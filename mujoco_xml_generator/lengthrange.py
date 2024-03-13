from interface import _ToString
import enum


class LengthRange(_ToString):
    class Mode(enum.Enum, _ToString):
        NoneMode = 0
        Muscle = 1
        MuscleUser = 2
        All = 4

        def to_string(self) -> str:
            match self:
                case LengthRange.Mode.NoneMode:
                    return "none"
                case LengthRange.Mode.Muscle:
                    return "muscle"
                case LengthRange.Mode.MuscleUser:
                    return "muscleuser"
                case LengthRange.Mode.All:
                    return "all"
            raise "Unexpected error occurred."

    def __init__(
            self,
            mode: Mode = Mode.Muscle,
            useexisting: bool = True,
            uselimit: bool = False,
            accel: float = 20.0,
            maxforce: float = 0.0,
            timeconst: float = 1.0,
            timestep: float = 0.01,
            inttotal: float = 10.0,
            interval: float = 2.0,
            tolrange: float = 0.05
    ):
        self.mode: str = mode.to_string()
        self.useexisting: str = str(useexisting).lower()
        self.uselimit: str = str(uselimit).lower()
        self.accel: float = accel
        self.maxforce: float = maxforce
        self.timeconst: float = timeconst
        self.timestep: float = timestep
        self.inttotal: float = inttotal
        self.interval: float = interval
        self.tolrange: float = tolrange

    def to_string(self) -> str:
        res = "<lengthrange "
        res += f"mode=\"{self.mode}\" "
        res += f"useexisting=\"{self.useexisting}\" "
        res += f"accel={self.accel} "
        res += f"maxforce={self.maxforce} "
        res += f"timeconst={self.timeconst} "
        res += f"timestep={self.timestep} "
        res += f"inttotal={self.inttotal} "
        res += f"interval={self.interval} "
        res += f"tolrange={self.tolrange} "
        res += "/>"
        return res
