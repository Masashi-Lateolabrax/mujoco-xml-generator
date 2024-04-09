from mujoco_xml_generator import common, _utils as utils


class Adhesion(utils.MuJoCoElement):
    def __init__(
            self,
            body: str,
            name: str | None = None,
            class_: str | None = None,
            group: int = 0,
            forcelimited: common.BoolOrAuto = common.BoolOrAuto.AUTO,
            ctrlrange: tuple[float, float] = (0.0, 0.0),
            forcerange: tuple[float, float] = (0.0, 0.0),
            user: list[float] | None = None,
            gain: float = 1.0
    ):
        self.body = utils.Attribution("body", body, str)
        self.name = utils.Attribution("name", name, str)
        self.class_ = utils.Attribution("class", class_, str)
        self.group = utils.Attribution("group", group, int, 0)
        self.forcelimited = utils.Attribution("forcelimited", forcelimited, str, common.BoolOrAuto.AUTO)
        self.ctrlrange = utils.Attribution("ctrlrange", ctrlrange, float, (0.0, 0.0))
        self.forcerange = utils.Attribution("forcerange", forcerange, float, (0.0, 0.0))
        self.user = utils.Attribution("user", user, float)
        self.gain = utils.Attribution("gain", gain, float, 1.0)

    def get_element_name(self):
        return "adhesion"

    def get_attributions(self):
        return [
            self.body,
            self.name,
            self.class_,
            self.group,
            self.forcelimited,
            self.ctrlrange,
            self.forcerange,
            self.user,
            self.gain
        ]

    def get_children(self):
        return None

    def __str__(self) -> str:
        return f"<Adhesion{utils.arrange_attributions(self.get_attributions())}>"
