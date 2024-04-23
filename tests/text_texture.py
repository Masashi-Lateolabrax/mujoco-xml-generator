from mujoco_xml_generator import common
from mujoco_xml_generator.asset import Texture


def test_to_string():
    sample = Texture()
    answer = "<texture/>"
    assert sample.to_xml() == answer


def test_to_string_with_attributions():
    sample = Texture(
        "Texture",
        type_=common.TextureType.SKYBOX,
        file="file",
        width=10,
        rgb1=(1.0, 0.2, 0.5)
    )
    answer = "<texture name=\"Texture\" type=\"skybox\" file=\"file\" rgb1=\"1.0 0.2 0.5\" width=\"10\"/>"
    assert sample.to_xml() == answer
