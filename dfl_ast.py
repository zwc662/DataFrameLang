from abc import ABC, abstractmethod
import enum
from dfl_runtime import DFL_Variable
from dfl_type import DFL_TYPE, DFL_OPTIONAL_TYPE
from dfl_lib import *
 

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
    

class DFL_TERM_INT(DFL_AST_NODE):
    def __init__(self, arg: int):
        assert isinstance(arg, int)
        super(DFL_TERM_INT, self).__init__(1, arg)

class DFL_TERM_FLOAT(DFL_AST_NODE):
    def __init__(self, arg: float):
        assert isinstance(arg, float)
        super(DFL_TERM_FLOAT, self).__init__(2, arg)

class DFL_TERM_BOOL(DFL_AST_NODE):
    def __init__(self, arg: bool):
        assert isinstance(arg, bool)
        super(DFL_TERM_BOOL, self).__init__(3, arg)
    
class DFL_TERM_STRING(DFL_AST_NODE):
    def __init__(self, arg: str):
        assert isinstance(arg, str)
        super(DFL_TERM_STRING, self).__init__(4, arg)

class DFL_TERM_VARIABLE(DFL_AST_NODE):
    def __init__(self, arg: DFL_Variable):
        assert isinstance(arg, DFL_Variable)
        super(DFL_TERM_VARIABLE, self).__init__(5, arg)

class DFL_TERM_FUNCTION(DFL_AST_NODE):
    def __init__(self, var: DFL_Variable, body: DFL_AST_NODE):
        assert isinstance(var, DFL_TERM_VARIABLE)
        assert isinstance(body, DFL_AST_NODE)
        super(DFL_TERM_FUNCTION, self).__init__(6, var, body)
    
class DFL_TERM_APPLY(DFL_AST_NODE):
    def __init__(self, function: DFL_AST_NODE, arg: DFL_AST_NODE):
        assert isinstance(function, DFL_TERM_FUNCTION)
        assert isinstance(arg, DFL_AST_NODE)
        super(DFL_TERM_APPLY, self).__init__(7, function, arg)

class DFL_TERM_LET(DFL_AST_NODE):
    def __init__(self, var: DFL_Variable, type: DFL_OPTIONAL_TYPE, term: DFL_AST_NODE):
        assert isinstance(var, DFL_Variable)
        assert isinstance(type, DFL_TYPE) or (type is None)
        assert isinstance(term, DFL_AST_NODE)
        super(DFL_TERM_LET, self).__init__(8, var, type, term)

class DFL_TERM_OPERATION(DFL_AST_NODE):
    def __init__(self, oprt: str, oprd):#: Tuple):
        assert isinstance(oprt, str)
        #assert isinstance(Tuple, oprd)
        super(DFL_TERM_OPERATION, self).__init__(9, oprt, oprd)

class DFL_TERM_ITE(DFL_AST_NODE):
    def __init__(self, cond: DFL_AST_NODE, branch1: DFL_AST_NODE, branch2: DFL_AST_NODE):
        assert isinstance(cond, DFL_AST_NODE)
        assert isinstance(branch1, DFL_AST_NODE)
        assert isinstance(branch2, DFL_AST_NODE)
        super(DFL_TERM_ITE, self).__init__(10, cond, branch1, branch2)

class DFL_TERM_FIXPOINT(DFL_AST_NODE):
    def __init__(self, function: DFL_Variable, variable: DFL_Variable, arg_type: DFL_OPTIONAL_TYPE, return_type: DFL_OPTIONAL_TYPE, abstraction: DFL_AST_NODE):
        assert isinstance(function, DFL_Variable)
        assert isinstance(variable, DFL_Variable)
        assert isinstance(arg_type, DFL_OPTIONAL_TYPE)
        assert isinstance(return_type, DFL_OPTIONAL_TYPE)
        assert isinstance(abstraction, DFL_AST_NODE)
        super(DFL_TERM_FIXPOINT, self).__init__(11, function, variable, arg_type, return_type, abstraction)

class DFL_TERM_CONS(DFL_AST_NODE):    
    def __init__(self, head: DFL_AST_NODE, tail: DFL_AST_NODE):
        assert isinstance(head, DFL_AST_NODE)
        assert isinstance(tail, DFL_AST_NODE)
        super(DFL_TERM_CONS, self).__init__(12, head, tail)

class DFL_TERM_NIL(DFL_AST_NODE):
    def __init__(self):
        super(DFL_TERM_NIL, self).__init__(13)

class DFL_TERM_HEAD(DFL_AST_NODE):
    def __init__(self, lst: DFL_AST_NODE):
        assert isinstance(lst, DFL_AST_NODE)
        super(DFL_TERM_HEAD, self).__init__(14, lst)

class DFL_TERM_TAIL(DFL_AST_NODE):
    def __init__(self, lst: DFL_AST_NODE):
        assert isinstance(lst, DFL_AST_NODE)
        super(DFL_TERM_TAIL, self).__init__(15, lst)

class DFL_TERM_TUPLE(DFL_AST_NODE):
    def __init__(self, first: DFL_AST_NODE, second: DFL_AST_NODE):
        assert isinstance(first, DFL_AST_NODE)
        assert isinstance(second, DFL_AST_NODE)
        super(DFL_TERM_TUPLE, self).__init__(16, first, second)

class DFL_TERM_LOOP(DFL_AST_NODE):
    def __init__(self, num_iter: DFL_Variable, var: DFL_Variable, type: DFL_OPTIONAL_TYPE, body: DFL_AST_NODE):
        assert isinstance(num_iter, DFL_Variable)
        assert isinstance(var, DFL_Variable)
        assert isinstance(type, DFL_TYPE) or (type is None)
        assert isinstance(body, DFL_AST_NODE)
        super(DFL_TERM_LOOP, self).__init__(17, num_iter, var, type, body)
    

def test():
    var = DFL_TERM_VARIABLE(DFL_Variable.Declare("hahe"))
    term = DFL_TERM_APPLY(DFL_TERM_FUNCTION(var, DFL_TERM_OPERATION("++", var)), DFL_TERM_INT(1))
    print(term)

if __name__ == "__main__":
    test()