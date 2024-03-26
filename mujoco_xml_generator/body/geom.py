import enum
from mujoco_xml_generator import common, interface, _utils as utils


class Geom:
    class GeomType(enum.Enum):
        PLANE = 0
        H_FIELD = 1
        SPHERE = 2
        CAPSULE = 3
        ELLIPSOID = 4
        CYLINDER = 5
        BOX = 6
        MESH = 7
        SDF = 8

        def __str__(self) -> str:
            match self:
                case Geom.GeomType.PLANE:
                    return "plane"
                case Geom.GeomType.H_FIELD:
                    return "hfield"
                case Geom.GeomType.SPHERE:
                    return "sphere"
                case Geom.GeomType.CAPSULE:
                    return "capsule"
                case Geom.GeomType.ELLIPSOID:
                    return "ellipsoid"
                case Geom.GeomType.CYLINDER:
                    return "cylinder"
                case Geom.GeomType.BOX:
                    return "box"
                case Geom.GeomType.MESH:
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
            type_: GeomType | None = GeomType.SPHERE,
            contype: int | None = 1,
            conaffinity: int | None = 1,
            condim: int | None = 3,
            group: int | None = 0,
            priority: int | None = 0,
            size: tuple | None = (0.0, 0.0, 0.0),
            material: str | None = None,
            rgba: tuple[float, float, float, float] | None = (0.5, 0.5, 0.5, 1),
            friction: tuple[float, float, float] | None = (1.0, 0.005, 0.0001),
            mass: float | None = None,
            density: float | None = 1000,
            shellinertia: bool | None = False,
            solmix: float | None = 1.0,
            solref: tuple[float, float] | None = (0.02, 1.0),
            solimp: tuple[float, float, float, float, float] | None = (0.9, 0.95, 0.001, 0.5, 2.0),
            margin: float | None = 0.0,
            gap: float | None = 0.0,
            fromto: tuple[float, float, float, float, float, float] | None = None,
            pos: tuple[float, float, float] | None = (0.0, 0.0, 0.0),
            orientation: interface.Orientation | None = common.Orientation.Quaternion(1, 0, 0, 0),
            hfield: str | None = None,
            mesh: str | None = None,
            fitscale: float | None = 1.0,
            fluidshape: FluidShape | None = FluidShape.none,
            fluidcoef: tuple[float, float, float, float, float] | None = (0.5, 0.25, 1.5, 1.0, 1.0),
            user: list[float] | None = None
    ):
        self.name = utils.Attribution("name", name, str)
        self.class_ = utils.Attribution("class", class_, str)
        self.type_ = utils.Attribution("type", type_, str, Geom.GeomType.SPHERE)
        self.contype = utils.Attribution("contype", contype, int, 1)
        self.conaffinity = utils.Attribution("conaffinity", conaffinity, int, 1)
        self.condim = utils.Attribution("condim", condim, int, 3)
        self.group = utils.Attribution("group", group, int, 0)
        self.priority = utils.Attribution("priority", priority, int, 0)
        self.size = utils.Attribution("size", size, float, (0.0, 0.0, 0.0))
        self.material = utils.Attribution("material", material, str)
        self.rgba = utils.Attribution("rgba", rgba, float, (0.5, 0.5, 0.5, 1))
        self.friction = utils.Attribution("friction", friction, float, (1.0, 0.005, 0.0001))
        self.mass = utils.Attribution("mass", mass, float)
        self.density = utils.Attribution("density", density, float, 1000)
        self.shellinertia = utils.Attribution("shellinertia", shellinertia, bool, False)
        self.solmix = utils.Attribution("solmix", solmix, float, 1.0)
        self.solref = utils.Attribution("solref", solref, float, (0.02, 1.0))
        self.solimp = utils.Attribution("solimp", solimp, float, (0.9, 0.95, 0.001, 0.5, 2.0))
        self.margin = utils.Attribution("margin", margin, float, 0.0)
        self.gap = utils.Attribution("gap", gap, float, 0.0)
        self.fromto = utils.Attribution("fromto", fromto, float)
        self.pos = utils.Attribution("pos", pos, float, (0.0, 0.0, 0.0))
        self.orientation = utils.Attribution(orientation.get_type(), orientation, str,
                                             common.Orientation.Quaternion(1, 0, 0, 0))
        self.hfield = utils.Attribution("hfield", hfield, str)
        self.mesh = utils.Attribution("mesh", mesh, str)
        self.fitscale = utils.Attribution("fitscale", fitscale, float, 1.0)
        self.fluidshape = utils.Attribution("fluidshape", fluidshape, str, Geom.FluidShape.none)
        self.fluidcoef = utils.Attribution("fluidcoef", fluidcoef, float, (0.5, 0.25, 1.5, 1.0, 1.0))
        self.user = utils.Attribution("user", user, float)

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

        return f"<geom{attributions}/>"
