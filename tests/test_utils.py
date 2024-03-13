from mujoco_xml_generator.utils import *


def test_attributions_to_str():
    a = Attribution("test1", 20.5)
    b = Attribution("test2", None)
    c = Attribution("test3", 1)
    d = Attribution("test4", True)
    e = Attribution("test5", "true")

    assert a.to_string() == "test1=\"20.5\""
    assert b.to_string() == ""
    assert c.to_string() == "test3=\"1\""
    assert d.to_string() == "test4=\"true\""
    assert e.to_string() == "test5=\"true\""


def test_arrange_attributions():
    attributions = [
        Attribution("test1", 20.5),
        Attribution("test2", None),
        Attribution("test3", 1),
        Attribution("test4", True),
        Attribution("test5", "true")
    ]
    assert arrange_attributions(attributions) == "test1=\"20.5\" test3=\"1\" test4=\"true\" test5=\"true\""
