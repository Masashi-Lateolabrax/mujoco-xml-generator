import enum
from mujoco_xml_generator import common, interface, _utils as utils


class Geom:
    class GeomType(enum.Enum):
        Plane = 0
        HField = 1
        Sphere = 2
        Capsule = 3
        Ellipsoid = 4
        Cylinder = 5
        Box = 6
        Mesh = 7
        SDF = 8

        def __str__(self) -> str:
            match self:
                case Geom.GeomType.Plane:
                    return "plane"
                case Geom.GeomType.HField:
                    return "hfield"
                case Geom.GeomType.Sphere:
                    return "sphere"
                case Geom.GeomType.Capsule:
                    return "capsule"
                case Geom.GeomType.Ellipsoid:
                    return "ellipsoid"
                case Geom.GeomType.Cylinder:
                    return "cylinder"
                case Geom.GeomType.Box:
                    return "box"
                case Geom.GeomType.Mesh:
                    return "mesh"
                case Geom.GeomType.SDF:
                    return "sdf"
            raise "Unexpected error occurred."

    class FluidShape(enum.Enum):
        none = 0
        ellipsoid = 1

        def __str__(self) -> str:
            match self:
                case Geom.FluidShape.none:
                    return "none"
                case Geom.FluidShape.ellipsoid:
                    return "ellipsoid"
            raise "Unexpected error occurred."

    def __init__(
            self,
            name: str | None = None,
            class_: str | None = None,
            type_: GeomType = GeomType.Sphere,
            contype: int = 1,
            conaffinity: int = 1,
            condim: int = 3,
            group: int = 0,
            priority: int = 0,
            size: tuple = (0.0, 0.0, 0.0),
            material: str | None = None,
            rgba: tuple[float, float, float, float] = (0.5, 0.5, 0.5, 1),
            friction: tuple[float, float, float] = (1.0, 0.005, 0.0001),
            mass: float | None = None,
            density: float = 1000,
            shellinertia: bool = False,
            solmix: float = 1.0,
            solref: tuple[float, float] = (0.02, 1.0),
            solimp: tuple[float, float, float, float, float] = (0.9, 0.95, 0.001, 0.5, 2.0),
            margin: float = 0.0,
            gap: float = 0.0,
            fromto: tuple[float, float, float, float, float, float] | None = None,
            pos: tuple[float, float, float] = (0.0, 0.0, 0.0),
            orientation: interface.Orientation = common.Orientation.Quaternion(1, 0, 0, 0),
            hfield: str | None = None,
            mesh: str | None = None,
            fitscale: float = 1.0,
            fluidshape: FluidShape = FluidShape.none,
            fluidcoef: tuple[float, float, float, float, float] = (0.5, 0.25, 1.5, 1.0, 1.0),
            user: list[float] | None = None
    ):
        self.name = utils.Attribution("name", name)
        self.class_ = utils.Attribution("class", class_)
        self.type_ = utils.Attribution("type", utils.str_or_none(type_))
        self.contype = utils.Attribution("contype", contype)
        self.conaffinity = utils.Attribution("conaffinity", conaffinity)
        self.condim = utils.Attribution("condim", condim)
        self.group = utils.Attribution("group", group)
        self.priority = utils.Attribution("priority", priority)
        self.size = utils.Attribution("size", size)
        self.material = utils.Attribution("material", material)
        self.rgba = utils.Attribution("rgba", rgba)
        self.friction = utils.Attribution("friction", friction)
        self.mass = utils.Attribution("mass", mass)
        self.density = utils.Attribution("density", density)
        self.shellinertia = utils.Attribution("shellinertia", shellinertia)
        self.solmix = utils.Attribution("solmix", solmix)
        self.solref = utils.Attribution("solref", solref)
        self.solimp = utils.Attribution("solimp", solimp)
        self.margin = utils.Attribution("margin", margin)
        self.gap = utils.Attribution("gap", gap)
        self.fromto = utils.Attribution("fromto", fromto)
        self.pos = utils.Attribution("pos", pos)
        self.orientation = utils.Attribution(orientation.get_type(), utils.str_or_none(orientation))
        self.hfield = utils.Attribution("hfield", hfield)
        self.mesh = utils.Attribution("mesh", mesh)
        self.fitscale = utils.Attribution("fitscale", fitscale)
        self.fluidshape = utils.Attribution("fluidshape", utils.str_or_none(fluidshape))
        self.fluidcoef = utils.Attribution("fluidcoef", fluidcoef)
        self.user = utils.Attribution("user", user)

    def __str__(self) -> str:
        attributions = utils.arrange_attributions([
            self.name,
            self.class_,
            self.type_,
            self.contype,
            self.conaffinity,
            self.condim,
            self.group,
            self.priority,
            self.size,
            self.material,
            self.rgba,
            self.friction,
            self.mass,
            self.density,
            self.shellinertia,
            self.solmix,
            self.solref,
            self.solimp,
            self.margin,
            self.gap,
            self.fromto,
            self.pos,
            self.orientation,
            self.hfield,
            self.mesh,
            self.fitscale,
            self.fluidshape,
            self.fluidcoef,
            self.user
        ])

        return f"<geom {attributions} />"
