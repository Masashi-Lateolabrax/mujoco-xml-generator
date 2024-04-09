from mujoco_xml_generator import _utils as utils

from mujoco_xml_generator.actuator import Adhesion, Cylinder, Damper, General, IntVelocity, Motor, Muscle, Position, Velocity


class Actuator(utils.MuJoCoElement):
    SUPPORTED_CHILDREN_TYPES = [
        Adhesion, Cylinder, Damper, General, IntVelocity, Motor, Muscle, Position, Velocity
    ]

    def __init__(self):
        self.children = []

    def get_element_name(self):
        return "actuator"

    def get_attributions(self):
        return []

    def add_children(self, children: list):
        for c in children:
            if type(c) is not Actuator and type(c) not in Actuator.SUPPORTED_CHILDREN_TYPES:
                raise "Unsupported type is added."
            self.children.append(c)
        return self

    def get_children(self):
        return self.children

    def __str__(self) -> str:
        return f"<Actuator{utils.arrange_attributions(self.get_attributions())}>"
