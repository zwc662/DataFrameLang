from abc import ABC, abstractmethod
import enum
from dfl_runtime import DFL_Variable
from dfl_type import DFL_TYPE
from dfl_lib import *
from typing import Optional, Union

class DFL_AST_TOKEN(enum.Enum):
    EMPTY = 0
    INT = 1
    FLOAT = 2
    BOOL = 3
    STRING = 4
    VARIABLE = 5
    FUNCTION = 6
    APPLY = 7
    LET = 8
    OPRATION = 9
    ITE = 10
    FIXPOINT = 11
    CONS = 12
    NIL = 13
    HEAD = 14
    TAIL = 15
    TUPLE = 16
    LOOP = 17

    @classmethod
    def from_tag(cls, tag):
        for model in cls:
            if model.value == tag:
                return model
        raise NotImplementedError

class DFL_AST_NODE(ABC):
    def __init__(self, token, *args):
        self._token = token
        self._args = conv_2_tuple(args)

    @property
    def token(self):
        return self._token

    @property
    def args(self):
        return self._args

    @args.setter 
    def args(self, *args, **kwargs):
        raise NotImplementedError
    
    @token.setter
    def token(self, *args, **kwargs):
        raise NotImplementedError
    

class DFL_INT(DFL_AST_NODE):
    def __init__(self, args: int):
        super(DFL_INT, self).__init__(1, args)

class DFL_FLOAT(DFL_AST_NODE):
    def __init__(self, args: float):
        super(DFL_FLOAT, self).__init__(2, args)

class DFL_BOOL(DFL_AST_NODE):
    def __init__(self, args: bool):
        super(DFL_BOOL, self).__init__(3, args)
    
class DFL_STRING(DFL_AST_NODE):
    def __init__(self, args: str):
        super(DFL_STRING, self).__init__(4, args)

class DFL_VARIABLE(DFL_AST_NODE):
    def __init__(self, args: DFL_Variable):
        super(DFL_VARIABLE, self).__init__(5, args)

class DFL_FUNCTION(DFL_AST_NODE):
    def __init__(self, input: DFL_AST_NODE, output: DFL_AST_NODE):
        super(DFL_FUNCTION, self).__init__(6, input, output)
    
class DFL_APPLY(DFL_AST_NODE):
    def __init__(self, abstraction: DFL_AST_NODE, args: DFL_AST_NODE):
        super(DFL_APPLY, self).__init__(7, abstraction, args)

class DFL_LET(DFL_AST_NODE):
    def __init__(self, variable: DFL_Variable, type: Optional[DFL_TYPE], term: DFL_AST_NODE):
        super(DFL_LET, self).__init__(8, variable, type, term)

class DFL_OPERATION(DFL_AST_NODE):
    def __init__(self, operator, operand: Tuple):
        super(DFL_OPERATION, self).__init__(9, operator, operand)

class DFL_ITE(DFL_AST_NODE):
    def __init__(self, cond: DFL_AST_NODE, branch1: DFL_AST_NODE, branch2: DFL_AST_NODE):
        super(DFL_ITE, self).__init__(10, cond, branch1, branch2)

class DFL_FIXPOINT(DFL_AST_NODE):
    def __init__(self, function: DFL_Variable, variable: DFL_Variable, arg_type: Optional[DFL_TYPE], return_type: Optional[DFL_TYPE], abstraction: DFL_AST_NODE):
        super(DFL_FIXPOINT, self).__init__(11, function, variable, arg_type, return_type, abstraction)

class DFL_CONS(DFL_AST_NODE):    
    def __init__(self, head: DFL_AST_NODE, tail: DFL_AST_NODE):
        super(DFL_CONS, self).__init__(12, head, tail)

class DFL_NIL(DFL_AST_NODE):
    def __init__(self):
        super(DFL_NIL, self).__init__(13)

class DFL_HEAD(DFL_AST_NODE):
    def __init__(self, lst: DFL_AST_NODE):
        super(DFL_HEAD, self).__init__(14, lst)

class DFL_TAIL(DFL_AST_NODE):
    def __init__(self, lst: DFL_AST_NODE):
        super(DFL_TAIL, self).__init__(15, lst)

class DFL_TUPLE(DFL_AST_NODE):
    def __init__(self, first: DFL_AST_NODE, second: DFL_AST_NODE):
        super(DFL_TUPLE, self).__init__(16, first, second)

class DFL_LOOP(DFL_AST_NODE):
    def __init__(self, num_iter: DFL_Variable, variable: DFL_Variable, type: Optional[DFL_TYPE], term: DFL_AST_NODE):
        super(DFL_LOOP, self).__init__(17, num_iter, variable, type, term)
    
