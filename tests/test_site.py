from mujoco_xml_generator import common
from mujoco_xml_generator.body import Site


def test_to_string():
    sample = Site()
    answer = "<site/>"
    assert str(sample) == answer


def test_to_string_with_none():
    sample = Site(
        name="site",
        type_=common.GeomType.PLANE,
        size=(0.1, 0.2, 3.0),
        rgba=(0.5, 0.5, 0.5, 1),
        orientation=common.Orientation.Quaternion(1, 0, 0, 0)
    )
    assert sample.to_xml() == "<site name=\"site\" type=\"plane\" size=\"0.1 0.2 3.0\"/>"
