from mujoco_xml_generator import WorldBody, Body, Orientation


def test_to_string():
    sample = Body(
        name="MuJoCo Model",
        pos=(1.0, 2.0, 3.0),
        orientation=Orientation.AxisAngle(1, 0, 0, 1.5),
        mocap=False,
        gravcomp=1.0,
        user=None
    )
    assert sample.to_xml() == "<body name=\"MuJoCo Model\" pos=\"1.0 2.0 3.0\" axisangle=\"1.0 0.0 0.0 1.5\" gravcomp=\"1.0\"></body>"


def test_to_string_with_none():
    sample = Body(
        name="MuJoCo Model",
        orientation=None,
        mocap=None,
        gravcomp=None
    )
    assert sample.to_xml() == "<body name=\"MuJoCo Model\"></body>"


def test_to_string_for_world():
    sample = WorldBody()
    assert sample.to_xml() == "<worldbody></worldbody>"
