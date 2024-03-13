import abc


class _ToString(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def to_string(self) -> str:
        raise NotImplementedError()
