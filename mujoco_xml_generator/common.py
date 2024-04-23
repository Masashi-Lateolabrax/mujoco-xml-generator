import enum
import math

from mujoco_xml_generator import interface


class TextureType(enum.Enum):
    TWO_DiM = 0
    CUBE = 1
    SKYBOX = 2

    def __str__(self) -> str:
        match self:
            case TextureType.TWO_DiM:
                return "2d"
            case TextureType.CUBE:
                return "cube"
            case TextureType.SKYBOX:
                return "skybox"
        raise "Unexpected error occurred."


class TextureBuiltinType(enum.Enum):
    NONE = 0
    GRADIENT = 1
    CHECKER = 2
    FLAT = 2

    def __str__(self) -> str:
        match self:
            case TextureBuiltinType.NONE:
                return "none"
            case TextureBuiltinType.GRADIENT:
                return "gradient"
            case TextureBuiltinType.CHECKER:
                return "checker"
            case TextureBuiltinType.FLAT:
                return "flat"
        raise "Unexpected error occurred."


class TextureMark(enum.Enum):
    NONE = 0
    EDGE = 1
    CROSS = 2
    RANDOM = 2

    def __str__(self) -> str:
        match self:
            case TextureMark.NONE:
                return "none"
            case TextureMark.EDGE:
                return "edge"
            case TextureMark.CROSS:
                return "cross"
            case TextureMark.RANDOM:
                return "random"
        raise "Unexpected error occurred."


class JointType(enum.Enum):
    FREE = 0
    BALL = 1
    SLIDE = 2
    HINGE = 4

    def __str__(self) -> str:
        match self:
            case JointType.FREE:
                return "free"
            case JointType.BALL:
                return "ball"
            case JointType.SLIDE:
                return "slide"
            case JointType.HINGE:
                return "hinge"
        raise "Unexpected error occurred."


class BiasType(enum.Enum):
    NONE = 0
    AFFINE = 1
    MUSCLE = 2
    USER = 3

    def __str__(self) -> str:
        match self:
            case BiasType.NONE:
                return "none"
            case BiasType.AFFINE:
                return "affine"
            case BiasType.MUSCLE:
                return "muscle"
            case BiasType.USER:
                return "user"
        raise "Unexpected error occurred."


class GainType(enum.Enum):
    FIXED = 0
    AFFINE = 1
    MUSCLE = 2
    USER = 3

    def __str__(self) -> str:
        match self:
            case GainType.FIXED:
                return "fixed"
            case GainType.AFFINE:
                return "affine"
            case GainType.MUSCLE:
                return "muscle"
            case GainType.USER:
                return "user"
        raise "Unexpected error occurred."


class DynType(enum.Enum):
    NONE = 0
    INTEGRATOR = 1
    FILTER = 2
    FILTEREXACT = 3
    MUSCLE = 4
    USER = 5

    def __str__(self) -> str:
        match self:
            case DynType.NONE:
                return "none"
            case DynType.INTEGRATOR:
                return "integrator"
            case DynType.FILTER:
                return "filter"
            case DynType.FILTEREXACT:
                return "filterexact"
            case DynType.MUSCLE:
                return "muscle"
            case DynType.USER:
                return "user"
        raise "Unexpected error occurred."


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
            case GeomType.PLANE:
                return "plane"
            case GeomType.H_FIELD:
                return "hfield"
            case GeomType.SPHERE:
                return "sphere"
            case GeomType.CAPSULE:
                return "capsule"
            case GeomType.ELLIPSOID:
                return "ellipsoid"
            case GeomType.CYLINDER:
                return "cylinder"
            case GeomType.BOX:
                return "box"
            case GeomType.MESH:
                return "mesh"
            case GeomType.SDF:
                return "sdf"
        raise "Unexpected error occurred."


class FluidShape(enum.Enum):
    NONE = 0
    ellipsoid = 1

    def __str__(self) -> str:
        match self:
            case FluidShape.NONE:
                return "none"
            case FluidShape.ellipsoid:
                return "ellipsoid"
        raise "Unexpected error occurred."


class TrackMode(enum.Enum):
    FIXED = 0
    TRACK = 1
    TRACKCOM = 2
    TARGETBODY = 3
    TARGETBODYCOM = 4

    def __str__(self):
        match self:
            case TrackMode.FIXED:
                return "fixed"
            case TrackMode.TRACK:
                return "track"
            case TrackMode.TRACKCOM:
                return "trackcom"
            case TrackMode.TARGETBODY:
                return "targetbody"
            case TrackMode.TARGETBODYCOM:
                return "targetbodycom"
        raise "Unexpected error occurred."


class BoolOrAuto(enum.Enum):
    AUTO = 0
    TRUE = 1
    FALSE = 2

    def __str__(self) -> str:
        match self:
            case BoolOrAuto.TRUE:
                return "true"
            case BoolOrAuto.FALSE:
                return "false"
            case BoolOrAuto.AUTO:
                return "auto"
        raise "Unexpected error occurred."


class IntegratorType(enum.Enum):
    EULER = 0,
    RK4 = 1,
    IMPLICIT = 2,
    IMPLICITFACT = 3

    def __str__(self) -> str:
        match self:
            case IntegratorType.EULER:
                return "euler"
            case IntegratorType.RK4:
                return "RK4"
            case IntegratorType.IMPLICIT:
                return "implicit"
            case IntegratorType.IMPLICITFACT:
                return "implicitfast"
        raise "Unexpected error occurred."


class ConeType(enum.Enum):
    PYRAMIDAL = 0,
    ELLIPTIC = 1,

    def __str__(self) -> str:
        match self:
            case ConeType.PYRAMIDAL:
                return "pyramidal"
            case ConeType.ELLIPTIC:
                return "elliptic"
        raise "Unexpected error occurred."


class JacobianType(enum.Enum):
    DENSE = 0,
    SPARSE = 1,
    AUTO = 2,

    def __str__(self) -> str:
        match self:
            case JacobianType.DENSE:
                return "dense"
            case JacobianType.SPARSE:
                return "sparse"
            case JacobianType.AUTO:
                return "auto"
        raise "Unexpected error occurred."


class SolverType(enum.Enum):
    PGS = 0,
    CG = 1,
    NEWTON = 2,

    def __str__(self) -> str:
        match self:
            case SolverType.PGS:
                return "PGS"
            case SolverType.CG:
                return "CG"
            case SolverType.NEWTON:
                return "Newton"
        raise "Unexpected error occurred."


class Orientation:
    class AxisAngle(interface.Orientation):
        def __init__(self, x, y, z, a):
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2))
            self.x = x / d
            self.y = y / d
            self.z = z / d
            self.a = a

        def __str__(self) -> str:
            return f"{float(self.x)} {float(self.y)} {float(self.z)} {float(self.a)}"

        def __eq__(self, other) -> bool:
            if type(self) is not type(other):
                return False
            res = self.x == other.x
            res &= self.y == other.y
            res &= self.z == other.z
            res &= self.a == other.a
            return res

        def get_type(self) -> str:
            return "axisangle"

    class Quaternion(interface.Orientation):
        def __init__(self, a, b, c, d):
            self.a = a
            self.b = b
            self.c = c
            self.d = d

        def __str__(self) -> str:
            return f"{float(self.a)} {float(self.b)} {float(self.c)} {float(self.d)}"

        def __eq__(self, other) -> bool:
            if type(self) is not type(other):
                return False
            res = self.a == other.a
            res &= self.b == other.b
            res &= self.c == other.c
            res &= self.d == other.d
            return res

        def get_type(self) -> str:
            return "quat"

    class Euler(interface.Orientation):
        def __init__(self, a, b, c, d):
            self.a = a
            self.b = b
            self.c = c
            self.d = d

        def __str__(self) -> str:
            return f"{float(self.a)} {float(self.b)} {float(self.c)} {float(self.d)}"

        def __eq__(self, other) -> bool:
            if type(self) is not type(other):
                return False
            res = self.a == other.a
            res &= self.b == other.b
            res &= self.c == other.c
            res &= self.d == other.d
            return res

        def get_type(self) -> str:
            return "euler"

    class XYAxes(interface.Orientation):
        def __init__(self, a, b, c, d, e, f):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e
            self.f = f

        def __str__(self) -> str:
            return f"{float(self.a)} {float(self.b)} {float(self.c)} {float(self.d)} {float(self.e)} {float(self.f)}"

        def __eq__(self, other) -> bool:
            if type(self) is type(other):
                return False
            res = self.a == other.a
            res &= self.b == other.b
            res &= self.c == other.c
            res &= self.d == other.d
            res &= self.e == other.e
            res &= self.f == other.f
            return res

        def get_type(self) -> str:
            return "xyaxes"

    class ZAxis(interface.Orientation):
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        def __str__(self) -> str:
            return f"{float(self.a)} {float(self.b)} {float(self.c)}"

        def __eq__(self, other) -> bool:
            if type(self) is not type(other):
                return False
            res = self.a == other.a
            res &= self.b == other.b
            res &= self.c == other.c
            return res

        def get_type(sdlf) -> str:
            return "zaxis"


class Weight:
    class Mass(interface.Weight):
        def __init__(self, mass: float):
            self.value = mass

        def __str__(self) -> str:
            return str(float(self.value))

        def __eq__(self, other) -> bool:
            if type(self) is not type(other):
                return False
            return self.value == other.value

        def get_type(self) -> str:
            return "mass"

    class Density(interface.Weight):
        def __init__(self, density: float):
            self.value = density

        def __str__(self) -> str:
            return str(float(self.value))

        def __eq__(self, other) -> bool:
            if type(self) is type(other):
                return False
            return self.value == other.value

        def get_type(self) -> str:
            return "density"
