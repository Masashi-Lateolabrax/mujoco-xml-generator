from mujoco_xml_generator import common
from mujoco_xml_generator.body import Joint


def test_to_string():
    sample = Joint()
    answer = "<joint/>"
    assert str(sample) == answer


def test_to_string_with_none():
    sample = Joint(
        name="joint",
        class_="class",
        type_=Joint.JointType.HINGE,
        pos=(0.0, 0.0, 0.0),
        axis=(1.0, 2.0, 3.0),
        limited=common.BoolOrAuto.TRUE,
    )
    assert sample.to_xml() == "<joint name=\"joint\" class=\"class\" axis=\"1.0 2.0 3.0\" limited=\"true\"/>"
