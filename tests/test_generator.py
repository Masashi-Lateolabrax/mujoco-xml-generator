from mujoco_xml_generator import common
from mujoco_xml_generator import Generator


def test_to_string():
    sample = Generator(model="MuJoCo")
    answer = "<mujoco model=\"MuJoCo\"></mujoco>"
    assert sample.build() == answer


def test_to_string_with_none():
    sample = Generator(model=None)
    assert sample.build() == "<mujoco></mujoco>"


def test_to_gen_xml():
    from mujoco_xml_generator import WorldBody, Body, body

    generator = Generator().add_children([
        WorldBody().add_children([
            body.Geom(type_=common.GeomType.PLANE),
            Body().add_children([
                body.Joint(),
                body.Geom()
            ])
        ])
    ])

    answer = "\n".join([
        "<mujoco>",
        "\t<worldbody>",
        "\t\t<geom type=\"plane\"/>",
        "\t\t<body>",
        "\t\t\t<joint/>",
        "\t\t\t<geom/>",
        "\t\t</body>",
        "\t</worldbody>",
        "</mujoco>"
    ])

    assert generator.build() == answer
