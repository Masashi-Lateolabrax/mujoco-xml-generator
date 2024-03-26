from mujoco_xml_generator._utils import *


def test_attributions_to_str():
    a = Attribution("test1", 20.5, float)
    b = Attribution("test2", None, int)
    c = Attribution("test3", 1, int)
    d = Attribution("test4", True, bool)
    e = Attribution("test5", "true", bool)

    assert str(a) == "test1=\"20.5\""
    assert str(b) == ""
    assert str(c) == "test3=\"1\""
    assert str(d) == "test4=\"true\""
    assert str(e) == "test5=\"true\""


def test_arrange_attributions():
    attributions = [
        Attribution("test1", 20.5, float),
        Attribution("test2", None, int),
        Attribution("test3", 1, int),
        Attribution("test4", True, bool),
        Attribution("test5", "true", bool)
    ]
    assert arrange_attributions(attributions) == " test1=\"20.5\" test3=\"1\" test4=\"true\" test5=\"true\""
