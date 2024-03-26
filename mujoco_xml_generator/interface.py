import abc


class GetTypeInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __str__(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def __eq__(self, other) -> bool:
        raise NotImplemented

    @abc.abstractmethod
    def get_type(self) -> str:
        raise NotImplemented


class Orientation(GetTypeInterface, abc.ABC):
    pass


class Weight(GetTypeInterface, abc.ABC):
    pass
