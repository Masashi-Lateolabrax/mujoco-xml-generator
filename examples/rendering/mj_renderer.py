import tkinter as tk
import tkinter.ttk as ttk

import mujoco

import mujoco_xml_generator as mjc_gen
import mujoco_xml_generator.common as mjc_cmn
from mujoco_xml_generator import WorldBody, Body, body, Option

from mujoco_xml_generator.utils import FPSManager, MuJoCoView


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
                body.Joint(type_=body.Joint.JointType.FREE),
                body.Geom(type_=mjc_cmn.GeomType.SPHERE, size=(1,))
            ]),

            Body(
                pos=(1.0, 1.0, 0.6)
            ).add_children([
                body.Joint(type_=body.Joint.JointType.FREE),
                body.Geom(type_=mjc_cmn.GeomType.BOX, size=(0.5, 0.5, 0.5))
            ])
        ])
    ])
    xml = generator.build()
    print(xml)
    return xml


class _MuJoCoProcess:
    def __init__(self, xml, width, height):
        self.model = mujoco.MjModel.from_xml_string(xml)
        self.data = mujoco.MjData(self.model)
        self.renderer = mujoco.Renderer(self.model, height, width)

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
    def __init__(self, xml, width, height):
        super().__init__()

        self._mouse_pos = [0, 0]
        self._mouse_left = False
        self._shift_key = False
        self._prev_step_start = 0.0

        self._mujoco = _MuJoCoProcess(xml, width, height)
        self._fps_manager = FPSManager(self._mujoco.get_timestep(), 10)

        self.resizable(False, False)

        self._info_frame = _InfoView(self, self._mujoco.camera_names())
        self._info_frame.grid(row=0, column=0)

        self._mujoco_view = MuJoCoView(self, width, height)
        self._mujoco_view.enable_input()
        self._mujoco_view.grid(row=0, column=1)

        self._camera_view = MuJoCoView(self, width, height)
        self._camera_view.grid(row=0, column=2)

        self.after(1, self.step)

    def step(self, handler=lambda m, d: ()):
        self._fps_manager.record_start()
        interval = self._fps_manager.ave_interval
        do_rendering = self._fps_manager.render_or_not(self._mujoco.get_timestep())

        if do_rendering:
            self._mujoco.step()
            self._mujoco_view.render(self._mujoco.data, self._mujoco.renderer)

            cam_name = self._info_frame.camera_names.get()
            if cam_name != "":
                self._camera_view.camera = cam_name
            self._camera_view.render(self._mujoco.data, self._mujoco.renderer)
        else:
            self._mujoco.step()

        self._info_frame.interval_label.config(text=f"interval : {interval:.5f}")
        view_camera = self._mujoco_view.camera
        self._info_frame.camera_lookat_label.config(
            text=f"camera lookat :\n {view_camera.lookat[0]:.3f}\n {view_camera.lookat[1]:.3f}\n {view_camera.lookat[2]:.3f}"
        )
        self._info_frame.camera_distance_label.config(text=f"camera distance : {view_camera.distance:.5f}")
        self._info_frame.skip_rate_label.config(text=f"skip rate : {self._fps_manager.skip_rate:.5f}")

        handler(self._mujoco.model, self._mujoco.data)

        self._fps_manager.record_stop(do_rendering)

        time_until_next_step = (self._mujoco.get_timestep() - interval) * 1000
        if time_until_next_step > 1.0:
            self.after(int(time_until_next_step + 0.5), self.step)
        else:
            self.after(1, self.step)


if __name__ == '__main__':
    def main():
        app = App(gen_xml(), 640, 480)
        app.mainloop()


    main()
