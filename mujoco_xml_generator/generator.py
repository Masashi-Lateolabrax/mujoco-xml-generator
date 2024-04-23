from mujoco_xml_generator import _utils as utils

from mujoco_xml_generator import Actuator
from mujoco_xml_generator import Asset
from mujoco_xml_generator import WorldBody, Body
from mujoco_xml_generator import Visual
from mujoco_xml_generator import Default
from mujoco_xml_generator import Option


class Generator:
    SUPPORTED_CHILDREN_TYPES = [Actuator, Asset, WorldBody, Body, Visual, Default, Option]

    def __init__(self, model: str = "MuJoCo Model"):
        self.model = utils.Attribution("model", model, str, "MuJoCo Model")

        self.children = []

    def add_children(self, children: list):
        for c in children:
            if type(c) not in Generator.SUPPORTED_CHILDREN_TYPES:
                raise f"Unsupported type is added. : {c}"
            self.children.append(c)
        return self

    def build(self):
        attributions = utils.arrange_attributions([self.model])
        return utils.gen_xml("mujoco", attributions, self.children)
