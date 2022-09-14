from abc import ABC, abstractmethod
import enum

class DFL_AST_TOKEN(enum.Enum):
    EXIST = 0
    BASE = 1
    DATAFRAME = 2
    LIST = 3
    TUPLE = 4
    FUNCTION = 5


class _DFL_AST_NODE(ABC):
    def __init__(self, token, *value):
        self._token = token
        self._value = value
