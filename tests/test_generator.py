from mujoco_xml_generator import Generator


def test_to_string():
    sample = Generator(model="MuJoCo")
    answer = "<mujoco model=\"MuJoCo\">\n</mujoco>"
    assert sample.build() == answer


def test_to_string_with_none():
    sample = Generator(model=None)
    assert sample.build() == "<mujoco>\n</mujoco>"
