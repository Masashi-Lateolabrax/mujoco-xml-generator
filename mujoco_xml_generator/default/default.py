from mujoco_xml_generator import _utils as utils

from .geom import Geom


class Default(utils.MuJoCoElement):
    SUPPORTED_CHILDREN_TYPES = [Geom]

    def __init__(self, class_: str):
        self.class_ = utils.Attribution("class", class_, str)
        self.children = []

    def get_element_name(self):
        return "default"

    def get_attributions(self):
        return [self.class_]

    def add_children(self, children: list):
        for c in children:
            if type(c) is not Default and type(c) not in Default.SUPPORTED_CHILDREN_TYPES:
                raise "Unsupported type is added."
            self.children.append(c)
        return self

    def get_children(self):
        return self.children
