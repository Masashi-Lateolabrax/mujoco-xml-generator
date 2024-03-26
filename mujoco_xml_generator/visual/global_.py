from mujoco_xml_generator import _utils as utils


class Global(utils.MuJoCoElement):
    def __init__(
            self,
            fovy: float = 45,
            ipd: float = 0.068,
            azimuth: float = 90,
            elevation: float = -45,
            linewidth: float = 1,
            glow: float = 0.3,
            realtime: float = 1,
            offwidth: int = 640,
            offheight: int = 480,
            ellipsoidinertia: bool = False,
            bvactive: bool = True,
    ):
        self.fovy = utils.Attribution("fovy", fovy, float, 45)
        self.ipd = utils.Attribution("ipd", ipd, float, 0.068)
        self.azimuth = utils.Attribution("azimuth", azimuth, float, 90)
        self.elevation = utils.Attribution("elevation", elevation, float, -45)
        self.linewidth = utils.Attribution("linewidth", linewidth, float, 1)
        self.glow = utils.Attribution("glow", glow, float, 0.3)
        self.realtime = utils.Attribution("realtime", realtime, float, 1)
        self.offwidth = utils.Attribution("offwidth", offwidth, int, 640)
        self.offheight = utils.Attribution("offheight", offheight, int, 480)
        self.ellipsoidinertia = utils.Attribution("ellipsoidinertia", ellipsoidinertia, bool, False)
        self.bvactive = utils.Attribution("bvactive", bvactive, bool, True)

    def get_element_name(self):
        return "global"

    def get_attributions(self):
        return [
            self.fovy,
            self.ipd,
            self.azimuth,
            self.elevation,
            self.linewidth,
            self.glow,
            self.realtime,
            self.offwidth,
            self.offheight,
            self.ellipsoidinertia,
            self.bvactive
        ]

    def get_children(self):
        return None
