from mujoco_xml_generator import common, _utils as utils


class Material(utils.MuJoCoElement):
    def __init__(
            self,
            name: str | None = None,
            class_: str | None = None,
            texture: str = None,
            texrepeat: tuple[float, float] = (1.0, 1.0),
            texuniform: bool = False,
            emission: float = 0,
            specular: float = 0.5,
            shininess: float = 0.5,
            reflectance: float = 0.0,
            rgba: tuple[float, float, float, float] = (1.0, 1.0, 1.0, 1.0)
    ):
        self.name = utils.Attribution("name", name, str, )
        self.class_ = utils.Attribution("class", class_, str)
        self.texture = utils.Attribution("texture", texture, str)
        self.texrepeat = utils.Attribution("texrepeat", texrepeat, float, (1.0, 1.0))
        self.texuniform = utils.Attribution("texuniform", texuniform, bool, False)
        self.emission = utils.Attribution("emission", emission, float, 0)
        self.specular = utils.Attribution("specular", specular, float, 0.5)
        self.shininess = utils.Attribution("shininess", shininess, float, 0.5)
        self.reflectance = utils.Attribution("reflectance", reflectance, float, 0.0)
        self.rgba = utils.Attribution("rgba", rgba, float, (1.0, 1.0, 1.0, 1.0))

    def get_element_name(self):
        return "material"

    def get_attributions(self):
        return [
            self.name,
            self.class_,
            self.texture,
            self.texrepeat,
            self.texuniform,
            self.emission,
            self.specular,
            self.shininess,
            self.reflectance,
            self.rgba
        ]

    def get_children(self):
        return None

    def __str__(self) -> str:
        return f"f<Material{utils.arrange_attributions(self.get_attributions())}>"
