from mujoco_xml_generator import common
from mujoco_xml_generator.body import Geom


def test_to_string():
    sample = Geom()
    answer = "<geom/>"
    assert str(sample) == answer


def test_to_string_with_none():
    sample = Geom(
        name="geom",
        type_=Geom.GeomType.PLANE,
        contype=1,
        condim=2,
        priority=0,
        size=(0.1, 0.2, 3.0),
        rgba=(0.5, 0.5, 0.5, 1),
        mass=None,
        density=1000,
        orientation=common.Orientation.Quaternion(1, 0, 0, 0)
    )
    assert str(sample) == "<geom name=\"geom\" type=\"plane\" condim=\"2\" size=\"0.1 0.2 3.0\"/>"
