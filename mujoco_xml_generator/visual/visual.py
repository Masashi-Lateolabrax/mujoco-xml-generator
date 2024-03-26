from mujoco_xml_generator import _utils as utils

from .global_ import Global


class Visual(utils.MuJoCoElement):
    SUPPORTED_CHILDREN_TYPES = [Global]

    def __init__(self):
        self.children = []

    def get_element_name(self):
        return "visual"

    def get_attributions(self):
        return []

    def add_children(self, children: list[utils.MuJoCoElement]):
        for c in children:
            if type(c) not in Visual.SUPPORTED_CHILDREN_TYPES:
                raise "Unsupported type is added."
            self.children.append(c)
        return self

    def get_children(self):
        return self.children
