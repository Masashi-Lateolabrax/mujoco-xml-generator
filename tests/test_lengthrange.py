from mujoco_xml_generator.lengthrange import *


def test_to_string():
    sample = LengthRange()
    assert sample.to_string() == "<lengthrange mode=\"muscle\" useexisting=\"true\" uselimit=\"false\" accel=\"20.0\" maxforce=\"0.0\" timeconst=\"1.0\" timestep=\"0.01\" inttotal=\"10.0\" interval=\"2.0\" tolrange=\"0.05\" />"


def test_to_string_with_none():
    sample = LengthRange(
        mode=None,
        useexisting=False,
        uselimit=None,
        accel=None,
        maxforce=None,
        timeconst=1,
        timestep=0.01,
        inttotal=None,
        interval=None,
        tolrange=None
    )
    assert sample.to_string() == "<lengthrange useexisting=\"false\" timeconst=\"1\" timestep=\"0.01\" />"
