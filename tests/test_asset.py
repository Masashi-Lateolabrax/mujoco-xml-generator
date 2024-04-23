from mujoco_xml_generator import Asset


def test_to_string():
    sample = Asset()
    answer = "<asset></asset>"
    assert sample.to_xml() == answer
