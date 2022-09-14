from abc import ABC, abstractmethod
import enum
from types import NotImplementedType

class DFL_AST_TOKEN(enum.Enum):
    EXIST = 0
    BASE = 1
    LIST = 2
    FUNCTION = 3
    TUPLE = 4

    @classmethod
    def from_name(cls, name):
        for model in cls.model:
            if cls.model.name == name:
                return cls.model
        raise NotImplementedType

class DFL_AST_NODE(ABC):
    def __init__(self, token, *value):
        self._token = token
        self._value = value

    @property
    def token(self):
        return self._token

    @property
    def value(self):
        return self._value

    @value.setter 
    def value(self, *args, **kwargs):
        raise NotImplementedError
    
    @token.setter
    def token(self, *args, **kwargs):
        raise NotImplementedError
    

class DFL_BASE(DFL_AST_NODE):
                                                               