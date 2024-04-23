from mujoco_xml_generator import _utils as utils

from .texture import Texture
from .material import Material


class Asset(utils.MuJoCoElement):
    SUPPORTED_CHILDREN_TYPES = [Texture, Material]

    def __init__(self):
        self.children = []

    def get_element_name(self):
        return "asset"

    def get_attributions(self):
        return []

    def add_children(self, children: list):
        for c in children:
            if type(c) not in Asset.SUPPORTED_CHILDREN_TYPES:
                raise "Unsupported type is added."
            self.children.append(c)
        return self

    def get_children(self):
        return self.children

    def __str__(self) -> str:
        return f"<Asset{utils.arrange_attributions(self.get_attributions())}>"
