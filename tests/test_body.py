from mujoco_xml_generator import Body, Orientation


def test_to_string():
    sample = Body(
        name="MuJoCo Model",
        pos=(1.0, 2.0, 3.0),
        orientation=Orientation.AxisAngle(1, 0, 0, 1.5),
        mocap=False,
        gravcomp=1.0,
        user=None
    )
    answer = "\n".join([
        "<body name=\"MuJoCo Model\" pos=\"1.0 2.0 3.0\" axisangle=\"1.0 0.0 0.0 1.5\" mocap=\"false\" gravcomp=\"1.0\">",
        "</body>"
    ])
    assert str(sample) == answer


def test_to_string_with_none():
    sample = Body(
        name="MuJoCo Model",
        orientation=None,
        mocap=None,
        gravcomp=None
    )
    answer = "\n".join([
        "<body name=\"MuJoCo Model\">",
        "</body>"
    ])
    assert str(sample) == answer
