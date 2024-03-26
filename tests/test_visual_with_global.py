from mujoco_xml_generator import Visual
from mujoco_xml_generator import visual


def test_to_string():
    sample = Visual().add_children([
        visual.Global(fovy=30, ipd=0.068, azimuth=-90)
    ])
    answer = "\n".join([
        "<visual>",
        "\t<global fovy=\"30.0\" azimuth=\"-90.0\"/>",
        "</visual>"
    ])
    assert sample.to_xml() == answer
