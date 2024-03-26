from mujoco_xml_generator import common, interface, _utils as utils

from .geom import Geom
from .joint import Joint


class Body:
    SUPPORTED_CHILDREN_TYPES = [Geom, Joint]

    def __init__(
            self,
            name: str | None = None,
            childclass: str | None = None,
            pos: tuple[float, float, float] | None = None,
            orientation: interface.Orientation | None = common.Orientation.Quaternion(1, 0, 0, 0),
            mocap: bool | None = False,
            gravcomp: float | None = 0.0,
            user: list[float] | None = None
    ):
        self.name = utils.Attribution("name", name)
        self.childclass = utils.Attribution("childclass", childclass)
        self.pos = utils.Attribution("pos", pos)
        self.orientation = utils.Attribution(utils.get_type_or_none(orientation), utils.str_or_none(orientation))
        self.mocap = utils.Attribution("mocap", mocap)
        self.gravcomp = utils.Attribution("gravcomp", gravcomp)
        self.user = utils.Attribution("user", user)

        self.children = []

    def add_children(self, children: list):
        for c in children:
            if type(c) is not Body and type(c) not in Body.SUPPORTED_CHILDREN_TYPES:
                raise "Unsupported type is added."
            self.children.append(c)

    def __str__(self) -> str:
        attributions = utils.arrange_attributions([
            self.name,
            self.childclass,
            self.pos,
            self.orientation,
            self.mocap,
            self.gravcomp,
            self.user
        ])

        return utils.gen_xml("body", attributions, self.children)


class WorldBody:
    SUPPORTED_CHILDREN_TYPES = [Body, Geom]

    def __init__(self):
        self.children = []

    def add_children(self, children: list):
        for c in children:
            if type(c) not in WorldBody.SUPPORTED_CHILDREN_TYPES:
                raise "Unsupported type is added."
            self.children.append(c)

    def __str__(self) -> str:
        return utils.gen_xml("worldbody", "", self.children)
