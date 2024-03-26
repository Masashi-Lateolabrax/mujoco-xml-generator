import enum
from mujoco_xml_generator import _utils as utils


class LengthRange(utils.MuJoCoElement):
    class Mode(enum.Enum):
        NoneMode = 0
        Muscle = 1
        MuscleUser = 2
        All = 4

        def __str__(self) -> str:
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
            mode: Mode | None = Mode.Muscle,
            useexisting: bool | None = True,
            uselimit: bool | None = False,
            accel: float | None = 20.0,
            maxforce: float | None = 0.0,
            timeconst: float | None = 1.0,
            timestep: float | None = 0.01,
            inttotal: float | None = 10.0,
            interval: float | None = 2.0,
            tolrange: float | None = 0.05
    ):
        self.mode = utils.Attribution("mode", mode, str, LengthRange.Mode.Muscle)
        self.useexisting = utils.Attribution("useexisting", useexisting, bool, True)
        self.uselimit = utils.Attribution("uselimit", uselimit, bool, False)
        self.accel = utils.Attribution("accel", accel, float, 20.0)
        self.maxforce = utils.Attribution("maxforce", maxforce, float, 0.0)
        self.timeconst = utils.Attribution("timeconst", timeconst, float, 1.0)
        self.timestep = utils.Attribution("timestep", timestep, float, 0.01)
        self.inttotal = utils.Attribution("inttotal", inttotal, float, 10.0)
        self.interval = utils.Attribution("interval", interval, float, 2.0)
        self.tolrange = utils.Attribution("tolrange", tolrange, float, 0.05)

    def get_element_name(self):
        return "lengthrange"

    def get_attributions(self):
        return [
            self.mode,
            self.useexisting,
            self.uselimit,
            self.accel,
            self.maxforce,
            self.timeconst,
            self.timestep,
            self.inttotal,
            self.interval,
            self.tolrange
        ]

    def get_children(self):
        return None

    def __str__(self) -> str:
        return f"<lengthrange{utils.arrange_attributions(self.get_attributions())}/>"
