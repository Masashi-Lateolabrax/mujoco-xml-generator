from mujoco_xml_generator import common
from mujoco_xml_generator import Actuator, actuator


def test_to_string():
    sample = Actuator().add_children([
        actuator.General(
            name="name",
            class_="class",
            group=1,
            ctrllimited=common.BoolOrAuto.TRUE,
            forcelimited=common.BoolOrAuto.FALSE,
            actlimited=common.BoolOrAuto.TRUE,
            ctrlrange=(1.0, 2.0),
            forcerange=(1, 2),
            actrange=(0.1, 0.2),
            lengthrange=(2.0, 1),
            gear=(1.1, 0, 0, 0, 0, 0),
            cranklength=1.0,
            joint="joint",
            jointinparent="parent",
            site="site",
            refsite="ref",
            body="body",
            tendon="tendon",
            cranksite="csite",
            user=[0.0],
            actdim=1.0,
            dyntype=common.DynType.MUSCLE,
            gaintype=common.GainType.FIXED,
            biastype=common.BiasType.AFFINE,
            dynprm=[1.0],
            gainprm=[1.0, 2.0],
            biasprm=[3.0],
            actearly=True
        )
    ])
    answer = "".join([
        "<actuator>\n",
        "\t<general ",
        "name=\"name\" ",
        "class=\"class\" ",
        "group=\"1\" ",
        "ctrllimited=\"true\" ",
        "forcelimited=\"false\" ",
        "actlimited=\"true\" ",
        "ctrlrange=\"1.0 2.0\" ",
        "forcerange=\"1.0 2.0\" ",
        "actrange=\"0.1 0.2\" ",
        "lengthrange=\"2.0 1.0\" ",
        "gear=\"1.1 0.0 0.0 0.0 0.0 0.0\" ",
        "cranklength=\"1.0\" ",
        "joint=\"joint\" ",
        "jointinparent=\"parent\" ",
        "site=\"site\" ",
        "refsite=\"ref\" ",
        "body=\"body\" ",
        "tendon=\"tendon\" ",
        "cranksite=\"csite\" ",
        "user=\"0.0\" ",
        "actdim=\"1.0\" ",
        "dyntype=\"muscle\" ",
        "gaintype=\"fixed\" ",
        "biastype=\"affine\" ",
        "dynprm=\"1.0\" ",
        "gainprm=\"1.0 2.0\" ",
        "biasprm=\"3.0\" ",
        "actearly=\"true\"/>\n",
        "</actuator>"
    ])
    assert sample.to_xml() == answer


def test_to_string_with_default():
    sample = Actuator().add_children([
        actuator.General(
            name="name",
            group=0,
            ctrllimited=common.BoolOrAuto.TRUE,
            forcelimited=common.BoolOrAuto.FALSE,
            actlimited=common.BoolOrAuto.TRUE,
            ctrlrange=(1.0, 2.0),
            actrange=(0.1, 0.2),
            lengthrange=(2.0, 1),
            gear=(1.0, 0, 0, 0, 0, 0),
            cranklength=1.0,
            joint="joint",
            jointinparent="parent",
            refsite="ref",
            body="body",
            tendon="tendon",
            cranksite="csite",
            user=[0.0],
            actdim=1.0,
            dyntype=common.DynType.MUSCLE,
            dynprm=(1.0,),
            gainprm=[1.0, 2.0],
            biasprm=[3.0],
            actearly=True
        )
    ])
    answer = "".join([
        "<actuator>\n",
        "\t<general ",
        "name=\"name\" ",
        "ctrllimited=\"true\" ",
        "forcelimited=\"false\" ",
        "actlimited=\"true\" ",
        "ctrlrange=\"1.0 2.0\" ",
        "actrange=\"0.1 0.2\" ",
        "lengthrange=\"2.0 1.0\" ",
        "cranklength=\"1.0\" ",
        "joint=\"joint\" ",
        "jointinparent=\"parent\" ",
        "refsite=\"ref\" ",
        "body=\"body\" ",
        "tendon=\"tendon\" ",
        "cranksite=\"csite\" ",
        "user=\"0.0\" ",
        "actdim=\"1.0\" ",
        "dyntype=\"muscle\" ",
        "gainprm=\"1.0 2.0\" ",
        "biasprm=\"3.0\" ",
        "actearly=\"true\"/>\n",
        "</actuator>"
    ])
    assert sample.to_xml() == answer
