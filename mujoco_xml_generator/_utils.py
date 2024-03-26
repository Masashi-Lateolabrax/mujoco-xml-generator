from mujoco_xml_generator import interface


def get_type_or_none(x: interface.GetTypeInterface) -> str | None:
    if x is None:
        return None
    return x.get_type()


class Attribution:
    def __init__(self, name: str, value, force_type, default=None):
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
            if type(self.value) is bool:
                self.value = str(self.value).lower()

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


def gen_xml(element_name: str, attributions: str, children: list):
    xml = [f"<{element_name}{attributions}>", f"</{element_name}>"]
    if len(children) > 0:
        xml.insert(1, "\n".join(["\t" + str(c) for c in children]))
    return "\n".join(xml)
