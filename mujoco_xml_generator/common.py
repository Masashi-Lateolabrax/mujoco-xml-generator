import enum
import math

from mujoco_xml_generator import interface


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
            res = type(self) is type(other)
            res &= self.x == other.x
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
            res = type(self) is type(other)
            res &= self.a == other.a
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
            res = type(self) is type(other)
            res &= self.a == other.a
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
            res = type(self) is type(other)
            res &= self.a == other.a
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
            res = type(self) is type(other)
            res &= self.a == other.a
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
            res = type(self) is type(other)
            res &= self.value == other.value
            return res

        def get_type(self) -> str:
            return "mass"

    class Density(interface.Weight):
        def __init__(self, density: float):
            self.value = density

        def __str__(self) -> str:
            return str(float(self.value))

        def __eq__(self, other) -> bool:
            res = type(self) is type(other)
            res &= self.value == other.value
            return res

        def get_type(self) -> str:
            return "density"
