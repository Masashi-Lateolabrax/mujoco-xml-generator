import abc

import numpy as np

from collections.abc import Iterable
from mujoco_xml_generator import interface


class MuJoCoElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_element_name(self):
        raise NotImplemented

    @abc.abstractmethod
    def get_attributions(self):
        raise NotImplemented

    @abc.abstractmethod
    def get_children(self):
        raise NotImplemented

    def to_xml(self, prefix="") -> str:
        return gen_xml(
            self.get_element_name(),
            arrange_attributions(self.get_attributions()),
            self.get_children(),
            prefix
        )


def get_type_or_none(x: interface.GetTypeInterface) -> str | None:
    if x is None:
        return None
    return x.get_type()


class Attribution:
    def __init__(self, name: str, value, force_type, default=None):
        self.name: str = name

        if value is None:
            self.value = None
        elif isinstance(value, Iterable) and type(value) is not str:
            if default is not None and all([type(v) is type(d) and v == d for v, d in zip(value, default)]):
                self.value = None
            elif all([type(v) is bool for v in value]):
                self.value = " ".join(map(lambda x: str(x).lower(), value))
            elif force_type is bool:
                self.value = " ".join(map(lambda x: str(force_type(x)).lower(), value))
            elif isinstance(value, np.ndarray):
                value = value.flatten()
                self.value = " ".join(map(lambda x: str(force_type(x)), value))
                pass
            else:
                self.value = " ".join(map(lambda x: str(force_type(x)), value))
        else:
            if default is not None and type(value) is type(default) and value == default:
                self.value = None
            elif type(value) is bool:
                self.value = str(value).lower()
            elif force_type is bool:
                self.value = str(force_type(value)).lower()
            else:
                self.value = force_type(value)

    def is_none(self) -> bool:
        return self.value is None

    def __str__(self) -> str:
        if self.value is None:
            return ""
        return f"{self.name}=\"{self.value}\""


def arrange_attributions(attributions: list[Attribution]) -> str:
    if len(attributions) == 0:
        return ""

    res = [str(a) for a in filter(lambda x: not x.is_none(), attributions)]
    res.insert(0, "")
    return " ".join(res)


def gen_xml(element_name: str, attributions: str, children: list[MuJoCoElement] | None, prefix: str = ""):
    if children is None:
        return f"{prefix}<{element_name}{attributions}/>"
    elif len(children) == 0:
        return f"{prefix}<{element_name}{attributions}></{element_name}>"
    else:
        xml = [
            f"{prefix}<{element_name}{attributions}>",
            "\n".join([c.to_xml(prefix + "\t") for c in children]),
            f"{prefix}</{element_name}>"
        ]
        return "\n".join(xml)
