from mujoco_xml_generator import utils

from mujoco_xml_generator.body import Body


class Generator:
    SUPPORTED_CHILDREN_TYPES = [Body]

    def __init__(self, model: str = "MuJoCo Model"):
        self.model = utils.Attribution("model", model)

        self.children = []

    def add_child(self, child):
        for t in Generator.SUPPORTED_CHILDREN_TYPES:
            if type(child) is t:
                self.children.append(child)
                return self
        raise "Unsupported type is added."

    def build(self):
        attributions = utils.arrange_attributions([
            self.model
        ])

        return "\n".join([
            f"<model {attributions}>",
            "\t",
            "\n\t".join([str(c) for c in self.children]),
            "</model>"
        ])
