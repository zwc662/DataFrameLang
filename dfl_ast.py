from abc import ABC, abstractmethod
import enum

class DFL_AST_TOKEN(enum.Enum):
    BASE = 1
    


class _DFL_AST_NODE(ABC):
    def __init__(self, token, *value):
        self._token = token
        self._value = value