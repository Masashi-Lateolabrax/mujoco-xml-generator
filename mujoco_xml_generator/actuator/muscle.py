from mujoco_xml_generator import common, _utils as utils


class Muscle(utils.MuJoCoElement):
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
            user: list[float] | None = None,
            timeconst: tuple[float, float] = (0.01, 0.04),
            tausmooth: float = 0.0,
            range_: tuple[float, float] = (0.75, 1.05),
            force: float = -1.0,
            scale: float = 200.0,
            lmin: float = 0.5,
            lmax: float = 1.6,
            vmax: float = 1.5,
            fpmax: float = 1.3,
            fvmax: float = 1.2,
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
        self.tendon = utils.Attribution("tendon", tendon, str)
        self.cranksite = utils.Attribution("cranksite", cranksite, str)
        self.slidersite = utils.Attribution("slidersite", slidersite, str)
        self.user = utils.Attribution("user", user, float)

        self.timeconst = utils.Attribution("timeconst", timeconst, float, (0.01, 0.04))
        self.tausmooth = utils.Attribution("tausmooth", tausmooth, float, 0.0)
        self.range_ = utils.Attribution("range", range_, float, (0.75, 1.05))
        self.force = utils.Attribution("force", force, float, -1.0)
        self.scale = utils.Attribution("scale", scale, float, 200.0)
        self.lmin = utils.Attribution("lmin", lmin, float, 0.5)
        self.lmax = utils.Attribution("lmax", lmax, float, 1.6)
        self.vmax = utils.Attribution("vmax", vmax, float, 1.5)
        self.fpmax = utils.Attribution("fpmax", fpmax, float, 1.3)
        self.fvmax = utils.Attribution("fvmax", fvmax, float, 1.2)

    def get_element_name(self):
        return "muscle"

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
            self.tendon,
            self.cranksite,
            self.user,
            self.timeconst,
            self.tausmooth,
            self.range_,
            self.force,
            self.scale,
            self.lmin,
            self.lmax,
            self.vmax,
            self.fpmax,
            self.fvmax,
        ]

    def get_children(self):
        return None

    def __str__(self) -> str:
        return f"<Muscle{utils.arrange_attributions(self.get_attributions())}>"
