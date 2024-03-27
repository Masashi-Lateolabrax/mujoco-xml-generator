from mujoco_xml_generator import common, _utils as utils


class Camera(utils.MuJoCoElement):
    def __init__(
            self,
            name: str | None = None,
            class_: str | None = None,
            mode: common.CameraMode | None = common.CameraMode.FIXED,
            target: str | None = None,
            resolution: tuple[int, int] | None = (1, 1),
            focal: tuple[float, float] | None = (0.0, 0.0),
            focalpixel: tuple[int, int] | None = (0, 0),
            principal: tuple[int, int] | None = (0, 0),
            principalpixel: tuple[float, float] | None = (0.0, 0.0),
            sensorsize: tuple[float, float] | None = (0.0, 0.0),
            ipd: float | None = 0.068,
            pos: tuple[float, float, float] | None = (0.0, 0.0, 0.0),
            orientation: common.Orientation | None = common.Orientation.Quaternion(1, 0, 0, 0),
            user: list[float] | None = None
    ):
        self.name = utils.Attribution("name", name, str)
        self.class_ = utils.Attribution("class", class_, str)
        self.mode = utils.Attribution("mode", mode, str, common.CameraMode.FIXED)
        self.target = utils.Attribution("target", target, str)
        self.resolution = utils.Attribution("resolution", resolution, int, (1, 1))
        self.focal = utils.Attribution("focal", focal, float, (0.0, 0.0))
        self.focalpixel = utils.Attribution("focalpixel", focalpixel, int, (0, 0))
        self.principal = utils.Attribution("principal", principal, int, (0, 0))
        self.principalpixel = utils.Attribution("principalpixel", principalpixel, float, (0.0, 0.0))
        self.sensorsize = utils.Attribution("sensorsize", sensorsize, float, (0.0, 0.0))
        self.ipd = utils.Attribution("ipd", ipd, float, 0.068, )
        self.pos = utils.Attribution("pos", pos, float, (0.0, 0.0, 0.0))
        self.orientation = utils.Attribution("orientation", orientation, str,
                                             common.Orientation.Quaternion(1, 0, 0, 0))
        self.user = utils.Attribution("user", user, float)

    def get_element_name(self):
        return "camera"

    def get_attributions(self):
        return [
            self.name,
            self.class_,
            self.mode,
            self.target,
            self.resolution,
            self.focal,
            self.focalpixel,
            self.principal,
            self.principalpixel,
            self.sensorsize,
            self.ipd,
            self.pos,
            self.orientation,
            self.user,
        ]

    def get_children(self):
        return None
