import enum

from lengthrange import LengthRange


class Compiler:
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
            inertiafromgeom: bool | None = None,  # None represents "auto".
            exactmeshinertia: bool = False,
            inertiagrouprange: tuple[int] = (0, 5)
    ):
        self.autolimits: str = str(autolimits).lower()
        self.boundmass: float = boundmass
        self.boundinertia: float = boundinertia
        self.settotalmass: float = settotalmass
        self.balanceinertia: str = str(balanceinertia).lower()
        self.strippath: str = str(strippath).lower()
        self.coordinate: str = coordinate.to_string()
        self.angle: str = angle.to_string()
        self.fitaabb: str = str(fitaabb).lower()
        self.eulerseq: str = eulerseq
        self.meshdir_: str = "" if meshdir is None else f"meshdir=\"{meshdir}\""
        self.texturedir_: str = "" if texturedir is None else f"texturedir=\"{texturedir}\""
        self.assetdir_: str = "" if assetdir is None else f"assetdir=\"{assetdir}\""
        self.discardvisual: str = str(discardvisual).lower()
        self.convexhull: str = str(convexhull).lower()
        self.usethread: str = str(usethread).lower()
        self.fusestatic: str = str(fusestatic).lower()
        self.inertiafromgeom: str = "auto" if inertiafromgeom is None else str(inertiafromgeom).lower()
        self.exactmeshinertia: str = str(exactmeshinertia).lower()
        self.inertiagrouprange: str = f"{inertiagrouprange[0]} {inertiagrouprange[1]}"

        self.children = []

    def add_child(self, child: LengthRange):
        supported_type_list = [LengthRange]
        is_supported = False
        for t in supported_type_list:
            is_supported |= type(child) is t
        self.children.append(child)

    def __str__(self) -> str:
        pass
