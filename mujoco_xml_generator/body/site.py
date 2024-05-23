from mujoco_xml_generator import common, interface, _utils as utils


class Site(utils.MuJoCoElement):
    def __init__(
            self,
            name: str | None = None,
            class_: str | None = None,
            type_: common.GeomType | None = common.GeomType.SPHERE,
            group: int | None = 0,
            material: str | None = None,
            rgba: tuple[float, float, float, float] | None = (0.5, 0.5, 0.5, 1),
            size: tuple | None = (0.005, 0.005, 0.005),
            fromto: tuple[float, float, float, float, float, float] | None = None,
            pos: tuple[float, float, float] | None = (0.0, 0.0, 0.0),
            orientation: interface.Orientation | None = common.Orientation.Quaternion(1, 0, 0, 0),
            user: list[float] | None = None
    ):
        self.name = utils.Attribution("name", name, str)
        self.class_ = utils.Attribution("class", class_, str)
        self.type_ = utils.Attribution("type", type_, str, common.GeomType.SPHERE)
        self.group = utils.Attribution("group", group, int, 0)
        self.size = utils.Attribution("size", size, float, (0.005, 0.005, 0.005))
        self.material = utils.Attribution("material", material, str)
        self.rgba = utils.Attribution("rgba", rgba, float, (0.5, 0.5, 0.5, 1))
        self.fromto = utils.Attribution("fromto", fromto, float)
        self.pos = utils.Attribution("pos", pos, float, (0.0, 0.0, 0.0))
        self.orientation = utils.Attribution(
            orientation.get_type(), orientation, str, common.Orientation.Quaternion(1, 0, 0, 0)
        )
        self.user = utils.Attribution("user", user, float)

    def get_element_name(self):
        return "site"

    def get_children(self):
        return None

    def get_attributions(self):
        return [
            self.name,
            self.class_,
            self.type_,
            self.group,
            self.size,
            self.material,
            self.rgba,
            self.fromto,
            self.pos,
            self.orientation,
            self.user
        ]

    def __str__(self) -> str:
        return f"<site{utils.arrange_attributions(self.get_attributions())}/>"
