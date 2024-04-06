from mujoco_xml_generator import common
from mujoco_xml_generator import Option


def test_to_string():
    sample = Option(
        timestep=0.005,
        impratio=0.0,
        wind=(1.0, 2.0, 3.0),
        viscosity=1.0,
        o_margin=1.0,
        o_solimp=(1.9, 0.95, 0.001, 0.5, 2.0),
        integrator=common.IntegratorType.EULER,
        cone=common.ConeType.ELLIPTIC,
        iterations=10,
        tolerance=1e-3,
        sdf_initpoints=41,
        actuatorgroupdisable=[1, 2, 3]
    )
    assert sample.to_xml() == "".join([
        "<option ",
        "timestep=\"0.005\" ",
        "impratio=\"0.0\" ",
        "wind=\"1.0 2.0 3.0\" ",
        "viscosity=\"1.0\" ",
        "o_margin=\"1.0\" ",
        "o_solimp=\"1.9 0.95 0.001 0.5 2.0\" ",
        "cone=\"elliptic\" ",
        "iterations=\"10\" ",
        "tolerance=\"0.001\" ",
        "sdf_initpoints=\"41\" ",
        "actuatorgroupdisable=\"1 2 3\"",
        "></option>"
    ])
