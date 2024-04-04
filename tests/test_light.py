from mujoco_xml_generator import common
from mujoco_xml_generator.body import Light


def test_to_string():
    sample = Light()
    assert sample.to_xml() == "<light/>"


def test_to_string_with_value():
    sample = Light(
        name="Light",
        mode=common.TrackMode.TRACK,
        target="Me",
        directional=True,
        castshadow=False,
        active=False,
        pos=(1.0, 2.0, 3.0),
        dir_=(-1.0, -2.0, -3.0),
        attenuation=(0.0, 1.0, 2.0),
        cutoff=60.0,
        exponent=11.0,
        ambient=(1.0, 1.1, 1.2),
        diffuse=(0.7, 0.8, 0.9),
        specular=(1.0, 2.0, 3.0)
    )
    assert sample.to_xml() == "".join([
        "<light name=\"Light\" mode=\"track\" target=\"Me\" directional=\"true\" ",
        "castshadow=\"false\" active=\"false\" pos=\"1.0 2.0 3.0\" dir=\"-1.0 -2.0 -3.0\" ",
        "attenuation=\"0.0 1.0 2.0\" cutoff=\"60.0\" exponent=\"11.0\" ambient=\"1.0 1.1 1.2\" ",
        "diffuse=\"0.7 0.8 0.9\" specular=\"1.0 2.0 3.0\"/>"
    ])


def test_to_string_with_none():
    sample = Light(
        name="Light",
        mode=common.TrackMode.TRACK,
        directional=True,
        castshadow=False,
        pos=(1.0, 2.0, 3.0),
        dir_=(-1.0, -2.0, -3.0),
        attenuation=(0.0, 1.0, 2.0),
        cutoff=60.0,
        ambient=(1.0, 1.1, 1.2),
        specular=(1.0, 2.0, 3.0)
    )
    assert sample.to_xml() == "".join([
        "<light name=\"Light\" mode=\"track\" directional=\"true\" ",
        "castshadow=\"false\" pos=\"1.0 2.0 3.0\" dir=\"-1.0 -2.0 -3.0\" ",
        "attenuation=\"0.0 1.0 2.0\" cutoff=\"60.0\" ambient=\"1.0 1.1 1.2\" ",
        "specular=\"1.0 2.0 3.0\"/>"
    ])
