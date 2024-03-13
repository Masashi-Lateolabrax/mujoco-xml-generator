from mujoco_xml_generator import utils
import enum


class LengthRange:
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
        self.mode = utils.Attribution("mode", utils.str_or_none(mode))
        self.useexisting = utils.Attribution("useexisting", useexisting)
        self.uselimit = utils.Attribution("uselimit", uselimit)
        self.accel = utils.Attribution("accel", accel)
        self.maxforce = utils.Attribution("maxforce", maxforce)
        self.timeconst = utils.Attribution("timeconst", timeconst)
        self.timestep = utils.Attribution("timestep", timestep)
        self.inttotal = utils.Attribution("inttotal", inttotal)
        self.interval = utils.Attribution("interval", interval)
        self.tolrange = utils.Attribution("tolrange", tolrange)

    def __str__(self) -> str:
        attributions = utils.arrange_attributions([
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
        ])
        return f"<lengthrange {attributions} />"
