from mujoco_xml_generator import _utils as utils


class HeadLight(utils.MuJoCoElement):
    def __init__(
            self,
            ambient: tuple[float, float, float] = (0.1, 0.1, 0.1),
            diffuse: tuple[float, float, float] = (0.4, 0.4, 0.4),
            specular: tuple[float, float, float] = (0.5, 0.5, 0.5),
            active: bool = True,
    ):
        self.ambient = utils.Attribution("ambient", ambient, float, (0.1, 0.1, 0.1))
        self.diffuse = utils.Attribution("diffuse", diffuse, float, (0.4, 0.4, 0.4))
        self.specular = utils.Attribution("specular", specular, float, (0.5, 0.5, 0.5))
        self.active = utils.Attribution("active", 1 if active else 0, int, 1)

    def get_element_name(self):
        return "headlight"

    def get_attributions(self):
        return [
            self.ambient,
            self.diffuse,
            self.specular,
            self.active
        ]

    def get_children(self):
        return None
