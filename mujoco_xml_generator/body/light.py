from mujoco_xml_generator import common, _utils as utils


class Light(utils.MuJoCoElement):
    def __init__(
            self,
            name: str | None = None,
            mode: common.TrackMode = common.TrackMode.FIXED,
            target: str | None = None,
            directional: bool = False,
            castshadow: bool = True,
            active: bool = True,
            pos: tuple[float, float, float] = (0.0, 0.0, 0.0),
            dir_: tuple[float, float, float] = (0.0, 0.0, -1.0),
            attenuation: tuple[float, float, float] = (1.0, 0.0, 0.0),
            cutoff: float = 45.0,
            exponent: float = 10.0,
            ambient: tuple[float, float, float] = (0.0, 0.0, 0.0),
            diffuse: tuple[float, float, float] = (0.7, 0.7, 0.7),
            specular: tuple[float, float, float] = (0.3, 0.3, 0.3),
    ):
        self.name = utils.Attribution("name", name, str)
        self.mode = utils.Attribution("mode", mode, str, common.TrackMode.FIXED)
        self.target = utils.Attribution("target", target, str)
        self.directional = utils.Attribution("directional", directional, bool, False)
        self.castshadow = utils.Attribution("castshadow", castshadow, bool, True)
        self.active = utils.Attribution("active", active, bool, True)
        self.pos = utils.Attribution("pos", pos, float, (0.0, 0.0, 0.0))
        self.dir_ = utils.Attribution("dir", dir_, float, (0.0, 0.0, -1.0))
        self.attenuation = utils.Attribution("attenuation", attenuation, float, (1.0, 0.0, 0.0))
        self.cutoff = utils.Attribution("cutoff", cutoff, float, 45.0)
        self.exponent = utils.Attribution("exponent", exponent, float, 10.0)
        self.ambient = utils.Attribution("ambient", ambient, float, (0.0, 0.0, 0.0))
        self.diffuse = utils.Attribution("diffuse", diffuse, float, (0.7, 0.7, 0.7))
        self.specular = utils.Attribution("specular", specular, float, (0.3, 0.3, 0.3))

    def get_element_name(self):
        return "light"

    def get_children(self):
        return None

    def get_attributions(self):
        return [
            self.name,
            self.mode,
            self.target,
            self.directional,
            self.castshadow,
            self.active,
            self.pos,
            self.dir_,
            self.attenuation,
            self.cutoff,
            self.exponent,
            self.ambient,
            self.diffuse,
            self.specular
        ]

    def __str__(self) -> str:
        return f"<light{utils.arrange_attributions(self.get_attributions())}/>"
