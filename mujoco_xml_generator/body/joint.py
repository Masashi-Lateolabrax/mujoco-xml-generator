import enum
from mujoco_xml_generator import common, interface, _utils as utils


class Joint(utils.MuJoCoElement):
    class JointType(enum.Enum):
        FREE = 0
        BALL = 1
        SLIDE = 2
        HINGE = 4

        def __str__(self) -> str:
            match self:
                case Joint.JointType.FREE:
                    return "free"
                case Joint.JointType.BALL:
                    return "ball"
                case Joint.JointType.SLIDE:
                    return "slide"
                case Joint.JointType.HINGE:
                    return "hinge"
            raise "Unexpected error occurred."

    def __init__(
            self,
            name: str | None = None,
            class_: str | None = None,
            type_: JointType | None = JointType.HINGE,
            group: int | None = 0,
            pos: tuple[float, float, float] | None = (0.0, 0.0, 0.0),
            axis: tuple[float, float, float] | None = (0.0, 0.0, 0.0),
            springdamper: tuple[float, float] | None = (0.0, 0.0),
            limited: common.BoolOrAuto | None = common.BoolOrAuto.AUTO,
            actuatorfrclimited: common.BoolOrAuto | None = common.BoolOrAuto.AUTO,
            solreflimit: tuple[float, float] | None = None,
            solimplimit: tuple[float, float, float, float, float] | None = None,
            solreffriction: tuple[float, float] | None = None,
            solimpfriction: tuple[float, float, float, float, float] | None = None,
            stiffness: float | None = 0.0,
            range_: tuple[float, float] | None = (0.0, 0.0),
            actuatorfrcrange: tuple[float, float] | None = (0.0, 0.0),
            margin: float | None = 0.0,
            ref: float | None = 0.0,
            springref: float | None = 0.0,
            armature: float | None = 0.0,
            damping: float | None = 0.0,
            frictionloss: float | None = 0.0,
            user: list[float] | None = None
    ):
        self.name = utils.Attribution("name", name, str)
        self.class_ = utils.Attribution("class", class_, str)
        self.type_ = utils.Attribution("type", type_, str, Joint.JointType.HINGE)
        self.group = utils.Attribution("group", group, int, 0)
        self.pos = utils.Attribution("pos", pos, float, (0.0, 0.0, 0.0))
        self.axis = utils.Attribution("axis", axis, float, (0.0, 0.0, 0.0))
        self.springdamper = utils.Attribution("springdamper", springdamper, float, (0.0, 0.0))
        self.limited = utils.Attribution("limited", limited, str, common.BoolOrAuto.AUTO)
        self.actuatorfrclimited = utils.Attribution("actuatorfrclimited", actuatorfrclimited, str,
                                                    common.BoolOrAuto.AUTO)
        self.solreflimit = utils.Attribution("solreflimit", solreflimit, float)
        self.solimplimit = utils.Attribution("solimplimit", solimplimit, float)
        self.solreffriction = utils.Attribution("solreffriction", solreffriction, float)
        self.solimpfriction = utils.Attribution("solimpfriction", solimpfriction, float)
        self.stiffness = utils.Attribution("stiffness", stiffness, float, 0.0)
        self.range_ = utils.Attribution("range_", range_, float, (0.0, 0.0))
        self.actuatorfrcrange = utils.Attribution("actuatorfrcrange", actuatorfrcrange, float, (0.0, 0.0))
        self.margin = utils.Attribution("margin", margin, float, 0.0)
        self.ref = utils.Attribution("ref", ref, float, 0.0)
        self.springref = utils.Attribution("springref", springref, float, 0.0)
        self.armature = utils.Attribution("armature", armature, float, 0.0)
        self.damping = utils.Attribution("damping", damping, float, 0.0)
        self.frictionloss = utils.Attribution("frictionloss", frictionloss, float, 0.0)
        self.user = utils.Attribution("user", user, float)

    def get_element_name(self):
        return "joint"

    def get_attributions(self):
        return [
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
        ]

    def __str__(self) -> str:
        return f"<joint{utils.arrange_attributions(self.get_attributions())}/>"

    def get_children(self):
        return None
