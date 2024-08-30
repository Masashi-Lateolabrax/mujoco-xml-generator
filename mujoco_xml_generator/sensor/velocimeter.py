from mujoco_xml_generator import common, _utils as utils


class Velocimeter(utils.MuJoCoElement):
    def __init__(
            self,
            site: str,
            name: str | None = None,
            noise: float = 0,
            cutoff: float = 0,
            user: list[float] | None = None,
    ):
        self.name = utils.Attribution("name", name, str)
        self.noise = utils.Attribution("noise", noise, float, 0)
        self.cutoff = utils.Attribution("cutoff", cutoff, float, 0)
        self.user = utils.Attribution("user", user, float)

        self.site = utils.Attribution("site", site, str)

    def get_element_name(self):
        return "velocimeter"

    def get_attributions(self):
        return [
            self.name,
            self.noise,
            self.cutoff,
            self.site,
            self.user,
        ]

    def get_children(self):
        return None

    def __str__(self) -> str:
        return f"<Velocimeter{utils.arrange_attributions(self.get_attributions())}>"
