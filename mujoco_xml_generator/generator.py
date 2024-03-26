from mujoco_xml_generator import _utils as utils

from mujoco_xml_generator import WorldBody, Body


class Generator:
    SUPPORTED_CHILDREN_TYPES = [WorldBody, Body]

    def __init__(self, model: str | None = "MuJoCo Model"):
        self.model = utils.Attribution("model", model)

        self.children = []

    def add_children(self, children: list):
        for c in children:
            if type(c) not in Generator.SUPPORTED_CHILDREN_TYPES:
                raise "Unsupported type is added."
            self.children.append(c)
        return self

    def build(self):
        attributions = utils.arrange_attributions([self.model])
        return utils.gen_xml("mujoco", attributions, self.children)
