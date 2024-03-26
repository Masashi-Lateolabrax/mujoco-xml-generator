from mujoco_xml_generator import Default, default


def test_to_string():
    sample = Default("sample").add_children([
        default.Geom(rgba=(1, 1, 1, 0.3))
    ])
    answer = "\n".join([
        "<default class=\"sample\">",
        "\t<geom rgba=\"1.0 1.0 1.0 0.3\"/>",
        "</default>"
    ])
    assert sample.to_xml() == answer
