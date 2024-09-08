from mujoco_xml_generator import _utils as utils

from .default import Default
from .geom import Geom


class TopDefault(utils.MuJoCoElement):
    SUPPORTED_CHILDREN_TYPES = [Default, Geom]

    def __init__(self, class_: str = None):
        self.class_ = utils.Attribution("class", class_, str, None)
        self.children = []

    def get_element_name(self):
        return "default"

    def get_attributions(self):
        return [self.class_]

    def add_children(self, children: list):
        for c in children:
            if type(c) not in TopDefault.SUPPORTED_CHILDREN_TYPES:
                raise "Unsupported type is added."
            self.children.append(c)
        return self

    def get_children(self):
        return self.children
