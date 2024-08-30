from mujoco_xml_generator import _utils as utils

from mujoco_xml_generator.sensor import Velocimeter


class Sensor(utils.MuJoCoElement):
    SUPPORTED_CHILDREN_TYPES = [
        Velocimeter
    ]

    def __init__(self):
        self.children = []

    def get_element_name(self):
        return "sensor"

    def get_attributions(self):
        return []

    def add_children(self, children: list):
        for c in children:
            if type(c) not in Sensor.SUPPORTED_CHILDREN_TYPES:
                raise "Unsupported type is added."
            self.children.append(c)
        return self

    def get_children(self):
        return self.children

    def __str__(self) -> str:
        return f"<Sensor{utils.arrange_attributions(self.get_attributions())}>"
