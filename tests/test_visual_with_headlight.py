from mujoco_xml_generator import Visual, visual


def test_to_string():
    sample = Visual().add_children([
        visual.HeadLight(ambient=(0.1, 0.1, 0.1), diffuse=(0.4, 0.4, 0.4), specular=(0.5, 0.5, 0.5), active=True)
    ])
    answer = "\n".join([
        "<visual>",
        "\t<headlight/>",
        "</visual>"
    ])
    assert sample.to_xml() == answer


def test_to_string2():
    sample = Visual().add_children([
        visual.HeadLight(ambient=(0.1, 0.2, 0.3), diffuse=(0.4, 0.5, 0.6), specular=(0.7, 0.8, 0.9), active=False)
    ])
    answer = "\n".join([
        "<visual>",
        "\t<headlight ambient=\"0.1 0.2 0.3\" diffuse=\"0.4 0.5 0.6\" specular=\"0.7 0.8 0.9\" active=\"0\"/>",
        "</visual>"
    ])
    assert sample.to_xml() == answer
