import enum

from mujoco_xml_generator import common, interface, _utils as utils


class Option(utils.MuJoCoElement):
    SUPPORTED_CHILDREN_TYPES = []

    def __init__(
            self,
            timestep: float = 0.002,
            apirate: float = 100.0,
            impratio: float = 1.0,
            gravity: tuple[float, float, float] = (0.0, 0.0, -9.81),
            wind: tuple[float, float, float] = (0.0, 0.0, 0.0),
            magnetic: tuple[float, float, float] = (0.0, -0.5, 0.0),
            density: float = 0.0,
            viscosity: float = 0.0,
            o_margin: float = 0.0,
            o_solref: tuple[float, float] = (0.02, 1.0),
            o_solimp: tuple[float, float, float, float, float] = (0.9, 0.95, 0.001, 0.5, 2.0),
            o_friction: tuple[float, float, float, float] | None = None,
            integrator: common.IntegratorType = common.IntegratorType.EULER,
            cone: common.ConeType = common.ConeType.PYRAMIDAL,
            jacobian: common.JacobianType = common.JacobianType.AUTO,
            solver: common.SolverType = common.SolverType.NEWTON,
            iterations: int = 100,
            tolerance: float = 1e-8,
            ls_iterations: int = 50,
            ls_tolerance: float = 0.01,
            noslip_iterations: int = 0,
            noslip_tolerance: float = 1e-6,
            mpr_iterations: int = 50,
            mpr_tolerance: float = 1e-6,
            sdf_iterations: int = 10,
            sdf_initpoints: int = 40,
            actuatorgroupdisable: list[int] | None = None,
    ):
        self.timestep = utils.Attribution("timestep", timestep, float, 0.002)
        self.apirate = utils.Attribution("apirate", apirate, float, 100.0)
        self.impratio = utils.Attribution("impratio", impratio, float, 1.0)
        self.gravity = utils.Attribution("gravity", gravity, float, (0.0, 0.0, -9.81))
        self.wind = utils.Attribution("wind", wind, float, (0.0, 0.0, 0.0))
        self.magnetic = utils.Attribution("magnetic", magnetic, float, (0.0, -0.5, 0.0))
        self.density = utils.Attribution("density", density, float, 0.0)
        self.viscosity = utils.Attribution("viscosity", viscosity, float, 0.0)
        self.o_margin = utils.Attribution("o_margin", o_margin, float, 0.0)
        self.o_solref = utils.Attribution("o_solref", o_solref, float, (0.02, 1.0))
        self.o_solimp = utils.Attribution("o_solimp", o_solimp, float, (0.9, 0.95, 0.001, 0.5, 2.0))
        self.o_friction = utils.Attribution("o_friction", o_friction, float)
        self.integrator = utils.Attribution("integrator", integrator, str, common.IntegratorType.EULER)
        self.cone = utils.Attribution("cone", cone, str, common.ConeType.PYRAMIDAL)
        self.jacobian = utils.Attribution("jacobian", jacobian, str, common.JacobianType.AUTO)
        self.solver = utils.Attribution("solver", solver, str, common.SolverType.NEWTON)
        self.iterations = utils.Attribution("iterations", iterations, int, 100)
        self.tolerance = utils.Attribution("tolerance", tolerance, float, 1e-8)
        self.ls_iterations = utils.Attribution("ls_iterations", ls_iterations, int, 50)
        self.ls_tolerance = utils.Attribution("ls_tolerance", ls_tolerance, float, 0.01)
        self.noslip_iterations = utils.Attribution("noslip_iterations", noslip_iterations, int, 0)
        self.noslip_tolerance = utils.Attribution("noslip_tolerance", noslip_tolerance, float, 1e-6)
        self.mpr_iterations = utils.Attribution("mpr_iterations", mpr_iterations, int, 50)
        self.mpr_tolerance = utils.Attribution("mpr_tolerance", mpr_tolerance, float, 1e-6)
        self.sdf_iterations = utils.Attribution("sdf_iterations", sdf_iterations, int, 10)
        self.sdf_initpoints = utils.Attribution("sdf_initpoints", sdf_initpoints, int, 40)
        self.actuatorgroupdisable = utils.Attribution("actuatorgroupdisable", actuatorgroupdisable, int)

        self.children = []

    def get_element_name(self):
        return "option"

    def get_attributions(self):
        return [
            self.timestep,
            self.apirate,
            self.impratio,
            self.gravity,
            self.wind,
            self.magnetic,
            self.density,
            self.viscosity,
            self.o_margin,
            self.o_solref,
            self.o_solimp,
            self.o_friction,
            self.integrator,
            self.cone,
            self.jacobian,
            self.solver,
            self.iterations,
            self.tolerance,
            self.ls_iterations,
            self.ls_tolerance,
            self.noslip_iterations,
            self.noslip_tolerance,
            self.mpr_iterations,
            self.mpr_tolerance,
            self.sdf_iterations,
            self.sdf_initpoints,
            self.actuatorgroupdisable
        ]

    def add_children(self, children: list):
        for c in children:
            if type(c) not in Option.SUPPORTED_CHILDREN_TYPES:
                raise "Unsupported type is added."
            self.children.append(c)
        return self

    def get_children(self):
        return self.children

    def __str__(self) -> str:
        return f"<Option{utils.arrange_attributions(self.get_attributions())}>"
