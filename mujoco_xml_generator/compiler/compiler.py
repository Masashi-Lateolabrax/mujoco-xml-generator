import enum
from mujoco_xml_generator import common, _utils as utils

from mujoco_xml_generator.compiler import LengthRange


class LocalOrGlobal(enum.Enum):
    Local = 0
    Global = 1

    def __str__(self) -> str:
        match self:
            case LocalOrGlobal.Local:
                return "local"
            case LocalOrGlobal.Global:
                return "global"
        raise "Unexpected error occurred."


class AngleType(enum.Enum):
    Radian = 0
    Degree = 1

    def __str__(self) -> str:
        match self:
            case AngleType.Radian:
                return "radian"
            case AngleType.Degree:
                return "degree"
        raise "Unexpected error occurred."


class Compiler(utils.MuJoCoElement):
    SUPPORTED_CHILDREN_TYPES = [LengthRange]

    def __init__(
            self,
            autolimits: bool = True,
            boundmass: float = 0.0,
            boundinertia: float = 0.0,
            settotalmass: float = -1.0,
            balanceinertia: bool = False,
            strippath: bool = False,
            coordinate: LocalOrGlobal = LocalOrGlobal.Local,
            angle: AngleType = AngleType.Degree,
            fitaabb: bool = False,
            eulerseq: str = "xyz",
            meshdir: str | None = None,
            texturedir: str | None = None,
            assetdir: str | None = None,
            discardvisual: bool = False,
            convexhull: bool = True,
            usethread: bool = True,
            fusestatic: bool = False,
            inertiafromgeom: common.BoolOrAuto = common.BoolOrAuto.AUTO,
            exactmeshinertia: bool = False,
            inertiagrouprange: tuple[int, int] = (0, 5)
    ):
        self.autolimits = utils.Attribution("autolimits", autolimits, bool, True)
        self.boundmass = utils.Attribution("boundmass", boundmass, float, 0.0)
        self.boundinertia = utils.Attribution("boundinertia", boundinertia, float, 0.0)
        self.settotalmass = utils.Attribution("settotalmass", settotalmass, float, -1.0)
        self.balanceinertia = utils.Attribution("balanceinertia", balanceinertia, bool, False)
        self.strippath = utils.Attribution("strippath", strippath, bool, False)
        self.coordinate = utils.Attribution("coordinate", coordinate, str, LocalOrGlobal.Local)
        self.angle = utils.Attribution("angle", angle, str, AngleType.Degree)
        self.fitaabb = utils.Attribution("fitaabb", fitaabb, bool, False)
        self.eulerseq = utils.Attribution("eulerseq", eulerseq, str, "xyz")
        self.meshdir = utils.Attribution("meshdir", meshdir, str, None)
        self.texturedir = utils.Attribution("texturedir", texturedir, str, None)
        self.assetdir = utils.Attribution("assetdir", assetdir, str, None)
        self.discardvisual = utils.Attribution("discardvisual", discardvisual, bool, False)
        self.convexhull = utils.Attribution("convexhull", convexhull, bool, True)
        self.usethread = utils.Attribution("usethread", usethread, bool, True)
        self.fusestatic = utils.Attribution("fusestatic", fusestatic, bool, False)
        self.inertiafromgeom = utils.Attribution("inertiafromgeom", inertiafromgeom, str, common.BoolOrAuto.AUTO)
        self.exactmeshinertia = utils.Attribution("exactmeshinertia", exactmeshinertia, bool, False)
        self.inertiagrouprange = utils.Attribution("inertiagrouprange", inertiagrouprange, int, (0, 5))

        self.children = []

    def get_element_name(self):
        return "compiler"

    def get_attributions(self):
        return [
            self.autolimits,
            self.boundmass,
            self.boundinertia,
            self.settotalmass,
            self.balanceinertia,
            self.strippath,
            self.coordinate,
            self.angle,
            self.fitaabb,
            self.eulerseq,
            self.meshdir,
            self.texturedir,
            self.assetdir,
            self.discardvisual,
            self.convexhull,
            self.usethread,
            self.fusestatic,
            self.inertiafromgeom,
            self.exactmeshinertia,
            self.inertiagrouprange
        ]

    def add_children(self, children: list):
        for c in children:
            if type(c) not in Compiler.SUPPORTED_CHILDREN_TYPES:
                raise "Unsupported type is added."
            self.children.append(c)
        return self

    def get_children(self):
        return self.children

    def __str__(self) -> str:
        return f"f<compiler{utils.arrange_attributions(self.get_attributions())}>"
