import enum
from mujoco_xml_generator import common, _utils as utils


class Joint:
    class JointType(enum.Enum):
        Free = 0
        Ball = 1
        Slide = 2
        Hinge = 4

        def __str__(self) -> str:
            match self:
                case Joint.JointType.Free:
                    return "free"
                case Joint.JointType.Ball:
                    return "ball"
                case Joint.JointType.Slide:
                    return "slide"
                case Joint.JointType.Hinge:
                    return "hinge"
            raise "Unexpected error occurred."

    def __init__(
            self,
            name: str | None = None,
            class_: str | None = None,
            type_: JointType = JointType.Hinge,
            group: int = 0,
            pos: tuple[float, float, float] = (0.0, 0.0, 0.0),
            axis: tuple[float, float, float] = (0.0, 0.0, 0.0),
            springdamper: tuple[float, float] = (0.0, 0.0),
            limited: common.BoolOrAuto = common.BoolOrAuto.AUTO,
            actuatorfrclimited: common.BoolOrAuto = common.BoolOrAuto.AUTO,
            solreflimit: tuple[float, float] | None = None,
            solimplimit: tuple[float, float, float, float, float] | None = None,
            solreffriction: tuple[float, float] | None = None,
            solimpfriction: tuple[float, float, float, float, float] | None = None,
            stiffness: float = 0.0,
            range_: tuple[float, float] = (0.0, 0.0),
            actuatorfrcrange: tuple[float, float] = (0.0, 0.0),
            margin: float = 0.0,
            ref: float = 0.0,
            springref: float = 0.0,
            armature: float = 0.0,
            damping: float = 0.0,
            frictionloss: float = 0.0,
            user: list[float] | None = None
    ):
        self.name = utils.Attribution("name", name)
        self.class_ = utils.Attribution("class", class_)
        self.type_ = utils.Attribution("type", utils.str_or_none(type_))
        self.group = utils.Attribution("group", group)
        self.pos = utils.Attribution("pos", pos)
        self.axis = utils.Attribution("axis", axis)
        self.springdamper = utils.Attribution("springdamper", springdamper)
        self.limited = utils.Attribution("limited", utils.str_or_none(limited))
        self.actuatorfrclimited = utils.Attribution("actuatorfrclimited", utils.str_or_none(actuatorfrclimited))
        self.solreflimit = utils.Attribution("solreflimit", solreflimit)
        self.solimplimit = utils.Attribution("solimplimit", solimplimit)
        self.solreffriction = utils.Attribution("solreffriction", solreffriction)
        self.solimpfriction = utils.Attribution("solimpfriction", solimpfriction)
        self.stiffness = utils.Attribution("stiffness", stiffness)
        self.range_ = utils.Attribution("range_", range_)
        self.actuatorfrcrange = utils.Attribution("actuatorfrcrange", actuatorfrcrange)
        self.margin = utils.Attribution("margin", margin)
        self.ref = utils.Attribution("ref", ref)
        self.springref = utils.Attribution("springref", springref)
        self.armature = utils.Attribution("armature", armature)
        self.damping = utils.Attribution("damping", damping)
        self.frictionloss = utils.Attribution("frictionloss", frictionloss)
        self.user = utils.Attribution("user", user)

    def __str__(self) -> str:
        attributions = utils.arrange_attributions([
            self.name,
            self.class_,
            self.type_,
            self.group,
            self.pos,
            self.axis,
            self.springdamper,
            self.limited,
            self.actuatorfrclimited,
            self.solreflimit,
            self.solimplimit,
            self.solreffriction,
            self.solimpfriction,
            self.stiffness,
            self.range_,
            self.actuatorfrcrange,
            self.margin,
            self.ref,
            self.springref,
            self.armature,
            self.damping,
            self.frictionloss,
            self.user,
        ])

        return f"<joint {attributions} />"
