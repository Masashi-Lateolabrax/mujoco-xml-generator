class Attribution:
    def __init__(self, name: str, value: float | int | bool | str | None = None):
        self.name: str = name
        self.value = value
        if type(self.value) is bool:
            self.value = str(self.value).lower()

    def is_none(self) -> bool:
        return self.value is None

    def __str__(self) -> str:
        if self.value is None:
            return ""
        return f"{self.name}=\"{self.value}\""


def arrange_attributions(attributions: list[Attribution]) -> str:
    res = ""
    for a in attributions:
        if a.is_none():
            continue
        res += str(a) + " "
    return res.rstrip()
