from .interface import _ToString


class Attribution(_ToString):
    def __init__(self, name: str, value: float | int | str | None = None):
        self.name: str = name
        self.value = value

    def to_string(self) -> str:
        if self.value is None:
            return ""
        return f"{self.name}=\"{self.value}\""


def arrange_attributions(attributions: list[Attribution]) -> str:
    res = ""
    for a in attributions:
        res += a.to_string() + " "
    return res.rstrip()
