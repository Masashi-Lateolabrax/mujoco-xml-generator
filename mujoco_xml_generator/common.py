import enum


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
