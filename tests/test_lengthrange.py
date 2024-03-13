from mujoco_xml_generator.lengthrange import *


def test_to_string():
    sample = LengthRange()
    assert sample.to_string() == "<lengthrange mode=\"muscle\" useexisting=\"true\" uselimit=\"false\" accel=\"20.0\" maxforce=\"0.0\" timeconst=\"1.0\" timestep=\"0.01\" inttotal=\"10.0\" interval=\"2.0\" tolrange=\"0.05\" />"

