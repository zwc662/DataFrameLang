from abc import ABC, abstractmethod
import enum
from dfl_lib import *
from typing import Optional, Union

class DFL_TYPE_TAG(enum.Enum):
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
        raise NotImplementedError

class DFL_TYPE(ABC):
    def __init__(self, tag, *value):
        self._constr = DFL_TYPE_TAG.from_tag(tag)
        self._argument = conv_2_tuple(value)

    @property
    def constructor(self):
        return self._constr

    @property
    def argument(self):
        return self._argument

    @argument.setter 
    def argument(self, *args, **kwargs):
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

DFL_OPTIONAL_TYPE = Optional[DFL_TYPE]

class DFL_TYPEVAR:
    def __init__(self, type: DFL_OPTIONAL_TYPE):
        assert isinstance(type, DFL_TYPE) or (type is None)
        if isinstance(type, DFL_TYPE):
            #assert hasattr(DFL_TYPE, 'constructor')
            #assert hasattr(DFL_TYPE, 'argument')
            #super(DFL_TYPEVAR, self).__init__(type.constructor.value, type.argument)
            self._val = type
        elif type is None:
            self._val = None
    
    @property
    def value(self):
        return self._val
    
    @value.setter
    def value(self, val):
        self._val = val

    def __eq__(self, other):
        assert self.value == other.value
    

    @classmethod
    def new(cls):
        return cls(None)

        
        
class DFL_TYPE_EXIST(DFL_TYPE):
    def __init__(self, var: DFL_TYPEVAR):
        assert isinstance(var, DFL_TYPEVAR)
        super(DFL_TYPE_EXIST, self).__init__(1, var)

class DFL_TYPE_BASE(DFL_TYPE):
    def __init__(self, arg):
        assert not isinstance(arg, DFL_TYPE)
        super(DFL_TYPE_BASE, self).__init__(2, arg)

class DFL_TYPE_LIST(DFL_TYPE):
    def __init__(self, arg: DFL_TYPE):
        assert isinstance(arg, DFL_TYPE)
        super(DFL_TYPE_LIST, self).__init__(3, arg)

class DFL_TYPE_REFERENCE(DFL_TYPE):
    def __init__(self, arg: DFL_TYPE):
        assert isinstance(arg, DFL_TYPE)
        super(DFL_TYPE_REFERENCE, self).__init__(4, arg)

class DFL_TYPE_FUNCTION(DFL_TYPE):
    def __init__(self, arg: DFL_TYPE, body: DFL_TYPE):
        assert isinstance(arg, DFL_TYPE)
        assert isinstance(body, DFL_TYPE)
        super(DFL_TYPE_FUNCTION, self).__init__(5, arg, body)

class DFL_TYPE_TUPLE(DFL_TYPE):
    def __init__(self, first: DFL_TYPE, second: DFL_TYPE):
        assert isinstance(first, DFL_TYPE)
        assert isinstance(second, DFL_TYPE)
        super(DFL_TYPE_TUPLE, self).__init__(6, first, second)

def test():
    type0 = DFL_TYPE_EXIST(DFL_TYPEVAR(None))
    type1 = DFL_TYPE_BASE(type(555))
    type2 = DFL_TYPE_LIST(type1)
    type3 = DFL_TYPE_REFERENCE(type2)
    type4 = DFL_TYPE_FUNCTION(type2, type3)
    type5 = DFL_TYPE_TUPLE(type3, type4)
    type6 = DFL_TYPE_TUPLE(type3, type4)
    type7 = DFL_TYPE_EXIST(DFL_TYPEVAR(type5))
    type8 = DFL_TYPE_EXIST(DFL_TYPEVAR(type6))
    for i in range(9):
        type_i = eval(f"type{i}")
        print(type_i, [getattr(type_i, attr) for attr in ['constructor', 'argument']])
    print(type7 == type8)
if __name__ == "__main__":
    test()