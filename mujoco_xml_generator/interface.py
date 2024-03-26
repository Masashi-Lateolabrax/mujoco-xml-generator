import abc


class Orientation(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __str__(self) -> str:
        return ""

    @abc.abstractmethod
    def get_type(self) -> str:
        return ""


class Weight(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __str__(self) -> str:
        return ""

    @abc.abstractmethod
    def get_type(self) -> str:
        return ""
