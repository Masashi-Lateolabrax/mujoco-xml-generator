from mujoco_xml_generator import common, _utils as utils


class General(utils.MuJoCoElement):
    def __init__(
            self,
            name: str | None = None,
            class_: str | None = None,
            group: int = 0,
            ctrllimited: common.BoolOrAuto = common.BoolOrAuto.AUTO,
            forcelimited: common.BoolOrAuto = common.BoolOrAuto.AUTO,
            actlimited: common.BoolOrAuto = common.BoolOrAuto.AUTO,
            ctrlrange: tuple[float, float] = (0.0, 0.0),
            forcerange: tuple[float, float] = (0.0, 0.0),
            actrange: tuple[float, float] = (0.0, 0.0),
            lengthrange: tuple[float, float] = (0.0, 0.0),
            gear: tuple[float, float, float, float, float, float] = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
            cranklength: float = 0.0,
            joint: str | None = None,
            jointinparent: str | None = None,
            site: str | None = None,
            refsite: str | None = None,
            body: str | None = None,
            tendon: str | None = None,
            cranksite: str | None = None,
            user: list[float] | None = None,
            actdim: float = -1.0,
            dyntype: common.DynType = common.DynType.NONE,
            gaintype: common.GainType = common.GainType.FIXED,
            biastype: common.BiasType = common.BiasType.NONE,
            dynprm: list[float] = (1.0,),
            gainprm: list[float] = (1.0,),
            biasprm: list[float] = (1.0,),
            actearly: bool = False,
    ):
        self.name = utils.Attribution("name", name, str)
        self.class_ = utils.Attribution("class", class_, str)
        self.group = utils.Attribution("group", group, int, 0)
        self.ctrllimited = utils.Attribution("ctrllimited", ctrllimited, str, common.BoolOrAuto.AUTO)
        self.forcelimited = utils.Attribution("forcelimited", forcelimited, str, common.BoolOrAuto.AUTO)
        self.actlimited = utils.Attribution("actlimited", actlimited, str, common.BoolOrAuto.AUTO)
        self.ctrlrange = utils.Attribution("ctrlrange", ctrlrange, float, (0.0, 0.0))
        self.forcerange = utils.Attribution("forcerange", forcerange, float, (0.0, 0.0))
        self.actrange = utils.Attribution("actrange", actrange, float, (0.0, 0.0))
        self.lengthrange = utils.Attribution("lengthrange", lengthrange, float, (0.0, 0.0))
        self.gear = utils.Attribution("gear", gear, float, (1.0, 0.0, 0.0, 0.0, 0.0, 0.0))
        self.cranklength = utils.Attribution("cranklength", cranklength, float, 0.0)
        self.joint = utils.Attribution("joint", joint, str)
        self.jointinparent = utils.Attribution("jointinparent", jointinparent, str)
        self.site = utils.Attribution("site", site, str)
        self.refsite = utils.Attribution("refsite", refsite, str)
        self.body = utils.Attribution("body", body, str)
        self.tendon = utils.Attribution("tendon", tendon, str)
        self.cranksite = utils.Attribution("cranksite", cranksite, str)
        self.user = utils.Attribution("user", user, float)
        self.actdim = utils.Attribution("actdim", actdim, float, -1.0)
        self.dyntype = utils.Attribution("dyntype", dyntype, str, common.DynType.NONE)
        self.gaintype = utils.Attribution("gaintype", gaintype, str, common.GainType.FIXED)
        self.biastype = utils.Attribution("biastype", biastype, str, common.BiasType.NONE)
        self.dynprm = utils.Attribution("dynprm", dynprm, float, (1.0,))
        self.gainprm = utils.Attribution("gainprm", gainprm, float, (1.0,))
        self.biasprm = utils.Attribution("biasprm", biasprm, float, (1.0,))
        self.actearly = utils.Attribution("actearly", actearly, bool, False)

    def get_element_name(self):
        return "general"

    def get_attributions(self):
        return [
            self.name,
            self.class_,
            self.group,
            self.ctrllimited,
            self.forcelimited,
            self.actlimited,
            self.ctrlrange,
            self.forcerange,
            self.actrange,
            self.lengthrange,
            self.gear,
            self.cranklength,
            self.joint,
            self.jointinparent,
            self.site,
            self.refsite,
            self.body,
            self.tendon,
            self.cranksite,
            self.user,
            self.actdim,
            self.dyntype,
            self.gaintype,
            self.biastype,
            self.dynprm,
            self.gainprm,
            self.biasprm,
            self.actearly,
        ]

    def get_children(self):
        return None

    def __str__(self) -> str:
        return f"<General{utils.arrange_attributions(self.get_attributions())}>"
