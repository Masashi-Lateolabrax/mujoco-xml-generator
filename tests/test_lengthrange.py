from mujoco_xml_generator.compiler import LengthRange


def test_to_string():
    sample = LengthRange()
    answer = "<lengthrange/>"
    assert str(sample) == answer


def test_to_string_with_none():
    sample = LengthRange(
        mode=None,
        useexisting=False,
        uselimit=None,
        accel=None,
        maxforce=None,
        timeconst=2,
        timestep=0.03,
        inttotal=None,
        interval=None,
        tolrange=None
    )
    assert sample.to_xml() == "<lengthrange useexisting=\"false\" timeconst=\"2.0\" timestep=\"0.03\"/>"
