from abc import ABC, abstractmethod
import enum
from types import NotImplementedType
from dfl_lib import *
from typing import Optional, Union

class DFL_TYPE_TAG(enum.Enum):
    OPTION = 0
    EXIST = 1
    BASE = 2
    LIST = 3
    REFERENCE = 4
    FUNCTION = 5
    TUPLE = 6

    @classmethod
    def from_tag(cls, tag):
        for model in cls:
            if model.value == tag:
                return model
        raise NotImplementedType

class DFL_TYPE(ABC):
    def __init__(self, tag, *type):
        self._constr = DFL_TYPE_TAG.from_tag(tag)
        self._type = conv_2_tuple(type)

    @property
    def constructor(self):
        return self._constr

    @property
    def args(self):
        return self._type

    @args.setter 
    def args(self, *args, **kwargs):
        raise NotImplementedError
    
    @constructor.setter
    def constructor(self, *args, **kwargs):
        raise NotImplementedError

"""
class DFL_Option(ABC):
    def __init__(self, type):
        self._type = type
    
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, *args, **kwargs):
        raise NotImplementedError 

class DFL_None(DFL_Option):
    def __init__(self):
        super(DFL_None, self).__init__(self, None)    

class DFL_Some(DFL_Option):
    def __init__(self, type):
        super(DFL_Some, self).__init__(type)
    
"""

class DFL_BASE(DFL_TYPE):
    def __init__(self, type):
        super(DFL_BASE, self).__init__(1, type)
