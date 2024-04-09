import time
import tkinter as tk

import mujoco
import numpy as np
from PIL import Image as PILImage, ImageTk as PILImageTk


class FPSManager:
    def __init__(self, target: float, n: int):
        self._n = n
        self._times: list[float] = []
        self._intervals_rendered: list[float] = []
        self._intervals_skipped: list[float] = []

        self.ave_interval_rendered = 0.0
        self.ave_interval_skipped = 0.0
        self.ave_interval = 0.0

        self._count: int = -n
        self.skip_rate: float = 1.0 / (n + 1)
        self._skip_tank: float = 0
        self._skip_co: list[float] = [1.0 / (n + 1), target, 1, 0.0018]

    def record_start(self):
        self._times.append(
            time.time()
        )
        if len(self._times) > self._n:
            self._times.pop(0)

    def record_stop(self, done_rendering):
        t = time.time()
        if done_rendering:
            self._intervals_rendered.append(t - self._times[-1])
            if len(self._intervals_rendered) > self._n:
                self._intervals_rendered.pop(0)
        else:
            self._intervals_skipped.append(t - self._times[-1])
            if len(self._intervals_skipped) > self._n:
                self._intervals_skipped.pop(0)

        if self._count >= self._n:
            self._count = 0
        self._count += 1

        r = self.ave_interval_rendered = sum(self._intervals_rendered) / self._n
        s = self.ave_interval_skipped = sum(self._intervals_skipped) / self._n
        self.ave_interval = r * (1 - self.skip_rate) + s * self.skip_rate

    def _update_skip_rate(self, target: float):
        r = self.ave_interval_rendered
        s = self.ave_interval_skipped
        self.skip_rate = (r - target) / (r - s)

    def render_or_not(self, target: float):
        if self._count == self._n:
            self._update_skip_rate(target)

        if self._skip_tank > 0:
            self._skip_tank -= 1
        if self._skip_tank <= 0 and self.skip_rate > 0.0:
            self._skip_tank += 1.0 / self.skip_rate
            return False

        return True


class MuJoCoView(tk.Frame):
    def __init__(self, master, width, height, cnf=None, **kw):
        if cnf is None:
            cnf = {}

        super().__init__(master, cnf, **kw)

        self._mouse_pos = [0, 0]
        self._mouse_left = False
        self.img_buf = np.zeros((height, width, 3), dtype=np.uint8)
        self.camera: mujoco.MjvCamera | str = mujoco.MjvCamera()

        self.canvas = tk.Canvas(master=self, width=width, height=height)
        self.canvas.pack(expand=True)

        plk_img_buf = PILImage.fromarray(
            np.zeros((height, width, 3), dtype=np.uint8)
        )
        self.tkimg_buf = PILImageTk.PhotoImage(image=plk_img_buf)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tkimg_buf)

    def enable_input(self):
        self.canvas.bind("<Motion>", self._mouse_move_handler)
        self.canvas.bind("<Shift-Motion>", self._mouse_shift_move_handler)
        self.canvas.bind("<MouseWheel>", lambda e: self._mouse_wheel_handler(e))
        self.canvas.bind("<ButtonPress-4>", lambda e: self._mouse_wheel_handler(e, "up"))
        self.canvas.bind("<ButtonPress-5>", lambda e: self._mouse_wheel_handler(e, "down"))
        self.canvas.bind("<Button-1>", lambda e: self._mouse_left_handler(e, "down"))
        self.canvas.bind("<ButtonRelease-1>", lambda e: self._mouse_left_handler(e, "up"))

    def _calc_camera_direction(self):
        quat = np.zeros((4,))
        v = np.zeros((3,))
        mujoco.mju_axisAngle2Quat(quat, [0, 1, 0], -mujoco.mjPI * self.camera.elevation / 180)
        mujoco.mju_rotVecQuat(v, [1, 0, 0], quat)
        mujoco.mju_axisAngle2Quat(quat, [0, 0, 1], mujoco.mjPI * self.camera.azimuth / 180)
        mujoco.mju_rotVecQuat(v, v, quat)
        return v

    def _calc_camera_up(self):
        quat = np.zeros((4,))
        v = np.zeros((3,))
        mujoco.mju_axisAngle2Quat(quat, [0, 1, 0], -mujoco.mjPI * self.camera.elevation / 180)
        mujoco.mju_rotVecQuat(v, [0, 0, 1], quat)
        mujoco.mju_axisAngle2Quat(quat, [0, 0, 1], mujoco.mjPI * self.camera.azimuth / 180)
        mujoco.mju_rotVecQuat(v, v, quat)
        return v

    def _mouse_wheel_handler(self, event, mode=None):
        sensitivity = 0.3

        v = self._calc_camera_direction()
        if mode == "up":
            self.camera.lookat += v * sensitivity
            return
        elif mode == "down":
            self.camera.lookat -= v * sensitivity
            return

    def _mouse_move_handler(self, event):
        dx = event.x - self._mouse_pos[0]
        dy = event.y - self._mouse_pos[1]
        self._mouse_pos[0] = event.x
        self._mouse_pos[1] = event.y

        if self._mouse_left:
            sensitivity = 0.1
            self.camera.elevation += dy * sensitivity
            self.camera.azimuth += dx * sensitivity

    def _mouse_shift_move_handler(self, event):
        dx = event.x - self._mouse_pos[0]
        dy = event.y - self._mouse_pos[1]
        self._mouse_pos[0] = event.x
        self._mouse_pos[1] = event.y

        if self._mouse_left:
            sensitivity = 0.01
            v = self._calc_camera_direction()
            up = self._calc_camera_up()
            left = np.cross(v, up)
            self.camera.lookat += up * sensitivity * dy
            self.camera.lookat -= left * sensitivity * dx

    def _mouse_left_handler(self, event, mode):
        self._mouse_left = mode == "down"

    def render(self, d: mujoco.MjData, renderer: mujoco.renderer.Renderer):
        renderer.update_scene(d, self.camera)
        renderer.render(out=self.img_buf)
        self.tkimg_buf.paste(
            PILImage.fromarray(self.img_buf)
        )
