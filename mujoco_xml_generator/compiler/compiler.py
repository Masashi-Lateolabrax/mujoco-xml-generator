import enum
from mujoco_xml_generator import common, _utils as utils

from mujoco_xml_generator.compiler import LengthRange


class Compiler:
    SUPPORTED_CHILDREN_TYPES = [LengthRange]

    class LocalOrGlobal(enum.Enum):
        Local = 0
        Global = 1

        def __str__(self) -> str:
            match self:
                case Compiler.LocalOrGlobal.Local:
                    return "local"
                case Compiler.LocalOrGlobal.Global:
                    return "global"
            raise "Unexpected error occurred."

    class AngleType(enum.Enum):
        Radian = 0
        Degree = 1

        def __str__(self) -> str:
            match self:
                case Compiler.AngleType.Radian:
                    return "radian"
                case Compiler.AngleType.Degree:
                    return "degree"
            raise "Unexpected error occurred."

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
        self.autolimits = utils.Attribution("autolimits", autolimits)
        self.boundmass = utils.Attribution("boundmass", boundmass)
        self.boundinertia = utils.Attribution("boundinertia", boundinertia)
        self.settotalmass = utils.Attribution("settotalmass", settotalmass)
        self.balanceinertia = utils.Attribution("balanceinertia", balanceinertia)
        self.strippath = utils.Attribution("strippath", strippath)
        self.coordinate = utils.Attribution("coordinate", utils.str_or_none(coordinate))
        self.angle = utils.Attribution("angle", utils.str_or_none(angle))
        self.fitaabb = utils.Attribution("fitaabb", fitaabb)
        self.eulerseq = utils.Attribution("eulerseq", eulerseq)
        self.meshdir = utils.Attribution("meshdir", meshdir)
        self.texturedir = utils.Attribution("texturedir", texturedir)
        self.assetdir = utils.Attribution("assetdir", assetdir)
        self.discardvisual = utils.Attribution("discardvisual", discardvisual)
        self.convexhull = utils.Attribution("convexhull", convexhull)
        self.usethread = utils.Attribution("usethread", usethread)
        self.fusestatic = utils.Attribution("fusestatic", fusestatic)
        self.inertiafromgeom = utils.Attribution("inertiafromgeom", utils.str_or_none(inertiafromgeom))
        self.exactmeshinertia = utils.Attribution("exactmeshinertia", exactmeshinertia)
        self.inertiagrouprange = utils.Attribution("inertiagrouprange", inertiagrouprange)

        self.children = []

    def add_children(self, children: list):
        for c in children:
            if type(c) not in Compiler.SUPPORTED_CHILDREN_TYPES:
                raise "Unsupported type is added."
            self.children.append(c)
        return self

    def __str__(self) -> str:
        attributions = utils.arrange_attributions([
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
        ])
        return "\n".join([
            f"<compiler {attributions}>",
            "\t",
            "\n\t".join([str(c) for c in self.children]),
            "</compiler>"
        ])
