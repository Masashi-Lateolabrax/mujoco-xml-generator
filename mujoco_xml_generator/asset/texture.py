from mujoco_xml_generator import common, _utils as utils


class Texture(utils.MuJoCoElement):
    def __init__(
            self,
            name: str | None = None,
            type_: common.TextureType = common.TextureType.CUBE,
            content_type: str | None = None,
            file: str | None = None,
            gridsize: tuple[int, int] = (1, 1),
            gridlayout: str = "............",
            # fileright,
            # fileleft,
            # fileup,
            # filedown,
            # filefront,
            # fileback,
            builtin: common.TextureBuiltinType = common.TextureBuiltinType.NONE,
            rgb1: tuple[float, float, float] = (0.8, 0.8, 0.8),
            rgb2: tuple[float, float, float] = (0.5, 0.5, 0.5),
            mark: common.TextureMark = common.TextureMark.NONE,
            markrgb: tuple[float, float, float] = (0.0, 0.0, 0.0),
            random: float = 0.01,
            width: int = 0,
            height: int = 0,
            hflip: bool = False,
            vflip: bool = False
    ):
        self.name = utils.Attribution("name", name, str)
        self.type_ = utils.Attribution("type", type_, str, common.TextureType.CUBE)
        self.content_type = utils.Attribution("content_type", content_type, str)
        self.file = utils.Attribution("file", file, str)
        self.gridsize = utils.Attribution("gridsize", gridsize, int, (1, 1))
        self.gridlayout = utils.Attribution("gridlayout", gridlayout, str, "............")
        self.builtin = utils.Attribution("builtin", builtin, str, common.TextureBuiltinType.NONE)
        self.rgb1 = utils.Attribution("rgb1", rgb1, float, (0.8, 0.8, 0.8))
        self.rgb2 = utils.Attribution("rgb2", rgb2, float, (0.5, 0.5, 0.5))
        self.mark = utils.Attribution("mark", mark, str, common.TextureMark.NONE)
        self.markrgb = utils.Attribution("markrgb", markrgb, float, (0.0, 0.0, 0.0))
        self.random = utils.Attribution("random", random, float, 0.01)
        self.width = utils.Attribution("width", width, int, 0)
        self.height = utils.Attribution("height", height, int, 0)
        self.hflip = utils.Attribution("hflip", hflip, bool, False)
        self.vflip = utils.Attribution("vflip", vflip, bool, False)

    def get_element_name(self):
        return "texture"

    def get_attributions(self):
        return [
            self.name,
            self.type_,
            self.content_type,
            self.file,
            self.gridsize,
            self.gridlayout,
            # self.fileright,
            # self.fileleft,
            # self.fileup,
            # self.filedown,
            # self.filefront,
            # self.fileback,
            self.builtin,
            self.rgb1,
            self.rgb2,
            self.mark,
            self.markrgb,
            self.random,
            self.width,
            self.height,
            self.hflip,
            self.vflip
        ]

    def get_children(self):
        return None

    def __str__(self) -> str:
        return f"f<texture{utils.arrange_attributions(self.get_attributions())}>"
