import abc


class GetTypeInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __str__(self) -> str:
        return ""

    @abc.abstractmethod
    def get_type(self) -> str:
        return ""


class Orientation(GetTypeInterface, abc.ABC):
    pass


class Weight(GetTypeInterface, abc.ABC):
    pass
