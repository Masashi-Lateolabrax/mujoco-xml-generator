from mujoco_xml_generator import Sensor, sensor


def test_velocimeter1():
    sample = Sensor().add_children([
        sensor.Velocimeter(
            site="site",
            name="name",
            noise=1,
            cutoff=2,
            user=[3, 4.0, 5],
        )
    ])
    answer = "".join([
        "<sensor>\n",
        "\t<velocimeter ",
        "name=\"name\" ",
        "noise=\"1.0\" ",
        "cutoff=\"2.0\" ",
        "site=\"site\" ",
        "user=\"3.0 4.0 5.0\"/>\n",
        "</sensor>"
    ])
    assert sample.to_xml() == answer


def test_velocimeter2():
    sample = Sensor().add_children([
        sensor.Velocimeter(
            site="site2",
        )
    ])
    answer = "".join([
        "<sensor>\n",
        "\t<velocimeter site=\"site2\"/>\n",
        "</sensor>"
    ])
    assert sample.to_xml() == answer
