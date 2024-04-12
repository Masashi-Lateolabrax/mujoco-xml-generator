import abc
import tkinter as tk
import tkinter.ttk as ttk

import mujoco
import numpy as np

import mujoco_xml_generator as mjc_gen
import mujoco_xml_generator.common as mjc_cmn
from mujoco_xml_generator.utils import FPSManager, MuJoCoView

from mujoco_xml_generator import Option
from mujoco_xml_generator import WorldBody, Body, body


def gen_xml() -> str:
    generator = mjc_gen.Generator().add_children([
        Option(timestep=0.007),

        WorldBody().add_children([
            body.Geom(
                type_=mjc_cmn.GeomType.PLANE, pos=(0, 0, 0), size=(10, 10, 1), rgba=(1, 1, 1, 1)
            ),

            Body(
                pos=(0, 0, 10)
            ).add_children([
                body.Joint(type_=mjc_cmn.JointType.FREE),
                body.Geom(type_=mjc_cmn.GeomType.SPHERE, size=(1,))
            ]),

            Body(
                pos=(1.0, 1.0, 0.6)
            ).add_children([
                body.Joint(type_=mjc_cmn.JointType.FREE),
                body.Geom(type_=mjc_cmn.GeomType.BOX, size=(0.5, 0.5, 0.5))
            ])
        ])
    ])
    xml = generator.build()
    print(xml)
    return xml


def main():
    app = App(gen_xml(), 640, 480)
    app.mainloop()


class ViewerHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def customize_tk(self, tk_top: tk.Tk):
        pass

    def renderer(self):
        pass

    @abc.abstractmethod
    def step(self, model: mujoco.MjModel, data: mujoco.MjData, gui: tk.Tk):
        raise NotImplementedError


class DefaultHandler(ViewerHandler):
    def customize_tk(self, tk_top: tk.Tk):
        pass

    def step(self, model: mujoco.MjModel, data: mujoco.MjData, gui: tk.Tk):
        pass


class _MuJoCoProcess:
    def __init__(self, xml, width, height):
        self.model = mujoco.MjModel.from_xml_string(xml)
        self.data = mujoco.MjData(self.model)

    def get_timestep(self) -> float:
        return self.model.opt.timestep

    def step(self):
        mujoco.mj_step(self.model, self.data)

    def camera_names(self):
        return [mujoco.mj_id2name(self.model, mujoco.mjtObj.mjOBJ_CAMERA, i) for i in range(self.model.ncam)]


class _InfoView(tk.Frame):
    def __init__(self, master, cameras: list[str], cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)

        def switch_move(x):
            self.do_simulate = x

        self.do_simulate = False
        tk.Button(self, text="start", command=lambda: switch_move(True)).pack()
        tk.Button(self, text="stop", command=lambda: switch_move(False)).pack()

        self.interval_label = tk.Label(self)
        self.interval_label.pack()

        self.skip_rate_label = tk.Label(self)
        self.skip_rate_label.pack()

        self.camera_lookat_label = tk.Label(self)
        self.camera_lookat_label.pack()

        self.camera_distance_label = tk.Label(self)
        self.camera_distance_label.pack()

        self.camera_names = ttk.Combobox(self, values=cameras, state="readonly")
        self.camera_names.pack()


class App(tk.Tk):
    def __init__(self, xml, width, height, handler: ViewerHandler = DefaultHandler()):
        super().__init__()

        if not isinstance(handler, ViewerHandler):
            raise "Please give an instance of ViewerHandler to the 'handler' argument."

        self._depth_img_buf = np.zeros((height, width), dtype=np.float32)

        self._mujoco = _MuJoCoProcess(xml, width, height)
        self._fps_manager = FPSManager(self._mujoco.get_timestep(), 60)

        self._renderer = mujoco.Renderer(self._mujoco.model, height, width)
        self._renderer_for_depth = mujoco.Renderer(self._mujoco.model, height, width)
        self._renderer_for_depth.enable_depth_rendering()

        self.resizable(False, False)

        self._info_frame = _InfoView(self, self._mujoco.camera_names())
        self._info_frame.grid(row=0, column=0, rowspan=2)

        self._mujoco_view = MuJoCoView(self, width, height)
        self._mujoco_view.enable_input()
        self._mujoco_view.grid(row=0, column=1)

        self._camera_view = MuJoCoView(self, width, height)
        self._camera_view.grid(row=0, column=2)

        self._depth_view = MuJoCoView(self, width, height)
        self._depth_view.grid(row=1, column=2)

        self.handler = handler
        self.handler.customize_tk(self)

        self.after(1, self.step)

    def step(self):
        interval = self._fps_manager.calc_interval()

        self._fps_manager.record_start()
        timestep = self._mujoco.get_timestep() - 0.001
        do_rendering = self._fps_manager.render_or_not(timestep)

        if self._info_frame.do_simulate:
            self._mujoco.step()
            self.handler.step(self._mujoco.model, self._mujoco.data, self)

        if do_rendering:
            cam_name = self._info_frame.camera_names.get()
            if cam_name != "":
                self._camera_view.camera = cam_name
                self._depth_view.camera = cam_name

            self._mujoco_view.render(self._mujoco.data, self._renderer)
            self._camera_view.render(self._mujoco.data, self._renderer)
            self._depth_view.render(self._mujoco.data, self._renderer_for_depth, self._depth_img_buf)

        self._info_frame.interval_label.config(text=f"interval : {interval:.5f}")
        self._info_frame.skip_rate_label.config(text=f"skip rate : {self._fps_manager.skip_rate:.5f}")
        view_camera = self._mujoco_view.camera
        self._info_frame.camera_lookat_label.config(
            text=f"camera lookat :\n {view_camera.lookat[0]:.3f}\n {view_camera.lookat[1]:.3f}\n {view_camera.lookat[2]:.3f}"
        )
        self._info_frame.camera_distance_label.config(text=f"camera distance : {view_camera.distance:.5f}")

        self._fps_manager.record_stop(do_rendering)

        time_until_next_step = (timestep - self._fps_manager.ave_interval) * 1000
        if time_until_next_step > 1.0:
            self.after(int(time_until_next_step), self.step)
        else:
            self.after(1, self.step)


if __name__ == '__main__':
    main()
