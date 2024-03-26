from mujoco_xml_generator import interface


def str_or_none(x) -> str | None:
    if x is None:
        return None
    return str(x)


def get_type_or_none(x: interface.GetTypeInterface) -> str | None:
    if x is None:
        return None
    return x.get_type()


class Attribution:
    def __init__(
            self, name: str, value: float | int | bool | tuple | list | str | None, force_type=lambda x: x, default=None
    ):
        self.name: str = name

        if value is None:
            self.value = None
        elif value == default:
            self.value = None
        elif type(value) is bool:
            self.value = str(value).lower()
        elif type(value) is tuple or type(value) is list:
            vs = []
            for v in value:
                if not (type(v) is int or type(v) is float):
                    raise "Specified type is unsupported."
                vs.append(str(force_type(v)))
            self.value = " ".join(vs)
        else:
            self.value = force_type(value)

    def is_none(self) -> bool:
        return self.value is None

    def __str__(self) -> str:
        if self.value is None:
            return ""
        return f"{self.name}=\"{self.value}\""


def arrange_attributions(attributions: list[Attribution]) -> str:
    return " ".join(str(a) for a in filter(lambda x: not x.is_none(), attributions))


def gen_xml(element_name: str, attributions: str, children: list):
    if len(attributions) > 0:
        attributions = " " + attributions
    xml = [f"<{element_name}{attributions}>", f"</{element_name}>"]
    if len(children) > 0:
        xml.insert(1, "\n".join(["\t" + str(c) for c in children]))
    return "\n".join(xml)
