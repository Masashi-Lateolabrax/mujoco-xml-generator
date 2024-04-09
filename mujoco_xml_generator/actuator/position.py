from mujoco_xml_generator import common, _utils as utils


class Position(utils.MuJoCoElement):
    def __init__(
            self,
            name: str | None = None,
            class_: str | None = None,
            group: int = 0,
            ctrllimited: common.BoolOrAuto = common.BoolOrAuto.AUTO,
            forcelimited: common.BoolOrAuto = common.BoolOrAuto.AUTO,
            ctrlrange: tuple[float, float] = (0.0, 0.0),
            forcerange: tuple[float, float] = (0.0, 0.0),
            lengthrange: tuple[float, float] = (0.0, 0.0),
            gear: tuple[float, float, float, float, float, float] = (1.0, 0.0, 0.0, 0.0, 0.0, 0.0),
            cranklength: float = 0.0,
            joint: str | None = None,
            jointinparent: str | None = None,
            tendon: str | None = None,
            cranksite: str | None = None,
            slidersite: str | None = None,
            site: str | None = None,
            refsite: str | None = None,
            user: list[float] | None = None,
            kp: float = 1.0,
            kv: float = 0.0,
            inheritrange: float = 0.0,
    ):
        self.name = utils.Attribution("name", name, str)
        self.class_ = utils.Attribution("class", class_, str)
        self.group = utils.Attribution("group", group, int, 0)
        self.ctrllimited = utils.Attribution("ctrllimited", ctrllimited, str, common.BoolOrAuto.AUTO)
        self.forcelimited = utils.Attribution("forcelimited", forcelimited, str, common.BoolOrAuto.AUTO)
        self.ctrlrange = utils.Attribution("ctrlrange", ctrlrange, float, (0.0, 0.0))
        self.forcerange = utils.Attribution("forcerange", forcerange, float, (0.0, 0.0))
        self.lengthrange = utils.Attribution("lengthrange", lengthrange, float, (0.0, 0.0))
        self.gear = utils.Attribution("gear", gear, float, (1.0, 0.0, 0.0, 0.0, 0.0, 0.0))
        self.cranklength = utils.Attribution("cranklength", cranklength, float, 0.0)
        self.joint = utils.Attribution("joint", joint, str)
        self.jointinparent = utils.Attribution("jointinparent", jointinparent, str)
        self.site = utils.Attribution("site", site, str)
        self.refsite = utils.Attribution("refsite", refsite, str)
        self.tendon = utils.Attribution("tendon", tendon, str)
        self.cranksite = utils.Attribution("cranksite", cranksite, str)
        self.slidersite = utils.Attribution("slidersite", slidersite, str)
        self.user = utils.Attribution("user", user, float)

        self.kp = utils.Attribution("kp", kp, float, 1.0)
        self.kv = utils.Attribution("kv", kv, float, 0.0)
        self.inheritrange = utils.Attribution("inheritrange", inheritrange, float, 0.0)

    def get_element_name(self):
        return "position"

    def get_attributions(self):
        return [
            self.name,
            self.class_,
            self.group,
            self.ctrllimited,
            self.forcelimited,
            self.ctrlrange,
            self.forcerange,
            self.lengthrange,
            self.gear,
            self.cranklength,
            self.joint,
            self.jointinparent,
            self.site,
            self.refsite,
            self.tendon,
            self.cranksite,
            self.user,
            self.kp,
            self.kv,
            self.inheritrange,
        ]

    def get_children(self):
        return None

    def __str__(self) -> str:
        return f"<Position{utils.arrange_attributions(self.get_attributions())}>"
