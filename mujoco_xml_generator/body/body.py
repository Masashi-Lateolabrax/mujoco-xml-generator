from mujoco_xml_generator import common, interface, _utils as utils

from .geom import Geom
from .joint import Joint
from .camera import Camera


class Body(utils.MuJoCoElement):
    SUPPORTED_CHILDREN_TYPES = [Geom, Joint, Camera]

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
        self.name = utils.Attribution("name", name, str)
        self.childclass = utils.Attribution("childclass", childclass, str)
        self.pos = utils.Attribution("pos", pos, float)
        self.orientation = utils.Attribution(utils.get_type_or_none(orientation), orientation, str,
                                             common.Orientation.Quaternion(1, 0, 0, 0))
        self.mocap = utils.Attribution("mocap", mocap, bool, False)
        self.gravcomp = utils.Attribution("gravcomp", gravcomp, float, 0.0)
        self.user = utils.Attribution("user", user, float)

        self.children = []

    def get_element_name(self):
        return "body"

    def get_attributions(self):
        return [
            self.name,
            self.childclass,
            self.pos,
            self.orientation,
            self.mocap,
            self.gravcomp,
            self.user
        ]

    def add_children(self, children: list):
        for c in children:
            if type(c) is not Body and type(c) not in Body.SUPPORTED_CHILDREN_TYPES:
                raise "Unsupported type is added."
            self.children.append(c)
        return self

    def get_children(self):
        return self.children

    def __str__(self) -> str:
        return f"<Body{utils.arrange_attributions(self.get_attributions())}>"


class WorldBody(utils.MuJoCoElement):
    SUPPORTED_CHILDREN_TYPES = [Body, Geom]

    def __init__(self):
        self.children = []

    def get_element_name(self):
        return "worldbody"

    def get_attributions(self):
        return []

    def add_children(self, children: list):
        for c in children:
            if type(c) not in WorldBody.SUPPORTED_CHILDREN_TYPES:
                raise "Unsupported type is added."
            self.children.append(c)
        return self

    def get_children(self):
        return self.children

    def __str__(self) -> str:
        return f"<WorldBody>"
