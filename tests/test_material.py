from mujoco_xml_generator.asset import Material


def test_to_string():
    sample = Material()
    assert sample.to_xml() == "<material/>"


def test_to_string2():
    sample = Material(
        name="material",
        class_="class",
        texture="texture",
        rgba=(1.0, 1.0, 1.0, 1.0),
        shininess=1.9,
        texrepeat=(0.9, 1),
        texuniform=True,
    )
    assert sample.to_xml() == "".join([
        "<material ",
        "name=\"material\" ",
        "class=\"class\" ",
        "texture=\"texture\" ",
        "texrepeat=\"0.9 1.0\" ",
        "texuniform=\"true\" ",
        "shininess=\"1.9\"",
        "/>"
    ])
