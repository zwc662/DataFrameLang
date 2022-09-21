import enum
from abc import ABC, abstractmethod
from dfl_lib import *
from dfl_ast import *
import pandas as pd
from pyspark import sql

"""This file defines the constant values in DFL
The values are defined by variant types. 
Each variant is identified by a constructor and isinstantiated by a concrete python constant.
"""

class DFL_VAL_TOKEN(enum.Enum):
    """DFL_VAL class is a enumerated type. Each component is a variant constructor with a tag.
    Each constructor will be used to identify the python constant.
    """
    Empty = 0
    PandasDataFrame = 1
    PandasGroupby = 2
    PandasIndex = 3
    SparkDataFrame = 4
    SparkColumn = 5
    Int = 6
    Float = 7
    Bool = 8
    String = 9
    Tuple = 10
    Function = 11
    FixPoint = 12
    Reference = 13
    CONS = 14
    NIL = 15
    
    @classmethod
    def from_tag(cls, tag):
        for model in cls:
            if model.value == tag:
                return model
        raise NotImplementedError

class DFL_VAL(ABC):
    """DFL_VAL is an abstract class used to define DFL constants. 
    Each constant contains a token (constructor) and a argument (content), which combines into a constructed data
    The abstract class must be concretized into different types of DFL constants.
    """
    def __init__(self, tag, *args):
        self._token = DFL_VAL_TOKEN.from_tag(tag)
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

    def __eq__(self, other):
        assert self.token == other.token
        assert len(self.args) == len(other.args)
        flg = True
        for i in range(len(self.args)):
            flg = flg and (self.args[i] == other.args[i])
        return flg

class DFL_CTXT:
    def __init__(self, head, tail):
        self.cons = tuple((head, tail))
    @property
    def head(self):
        return self.cons[0]
    @property
    def taili(self):
        return self.cons[1]
    
    
"""Below is a list of concrete DLF VAL constants. Each constant class is a sub-class of the parent abstract DFL_VAL class.
Different kinds of constansts have different constructors and different number of arguments
"""
class DFL_VAL_EMPTY(DFL_VAL):
    def __init__(self):
        super(DFL_VAL_EMPTY, self).__init__(0)

class DFL_VAL_PDF(DFL_VAL):
    def __init__(self, arg: pd.DataFrame):
        assert isinstance(arg, pd.DataFrame)
        super(DFL_VAL_PDF, self).__init__(1, arg)
 

class DFL_VAL_PGB(DFL_VAL):
    def __init__(self, arg: pd.DataFrame.groupby):
        assert isinstance(arg, pd.DataFrame.groupby)
        super(DFL_VAL_PGB, self).__init__(2, arg)

class DFL_VAL_PDI(DFL_VAL):
    def __init__(self, arg: pd.DataFrame.index):
        assert isinstance(arg, pd.DataFrame.index)
        super(DFL_VAL_PDI, self).__init__(3, arg)

class DFL_VAL_SDF(DFL_VAL):
    def __init__(self, arg: sql.DataFrame):
        assert isinstance(arg, sql.DataFrame)
        super(DFL_VAL_SDF, self).__init__(4, arg)

class DFL_VAL_SCOL(DFL_VAL):
    def __init__(self, arg: sql.Column):
        assert isinstance(arg, sql.Column)
        super(DFL_VAL_SCOL, self).__init__(5, arg)

class DFL_VAL_INT(DFL_VAL):
    def __init__(self, arg: int):
        assert isinstance(arg, int)
        super(DFL_VAL_INT, self).__init__(6, arg)

class DFL_VAL_FLOAT(DFL_VAL):
    def __init__(self, arg: float):
        assert isinstance(arg, float)
        super(DFL_VAL_FLOAT, self).__init__(7, arg)

class DFL_VAL_BOOL(DFL_VAL):
    def __init__(self, arg: bool):
        assert isinstance(arg, bool)
        super(DFL_VAL_BOOL, self).__init__(8, arg)
    
class DFL_VAL_STRING(DFL_VAL):
    def __init__(self, arg: str):
        assert isinstance(arg, str)
        super(DFL_VAL_STRING, self).__init__(9, arg)
 
class DFL_VAL_TUPLE(DFL_VAL):
    def __init__(self, arg1: DFL_VAL, arg2: DFL_VAL):
        assert isinstance(arg1, DFL_VAL) and isinstance(arg2, DFL_VAL)
        super(DFL_VAL_TUPLE, self).__init__(10, arg1, arg2)

class DFL_VAL_FUNCTION(DFL_VAL):
    def __init__(self, func: DFL_AST_NODE, ctxt: DFL_CTXT):
        assert isinstance(func, DFL_AST_NODE)
        assert isinstance(ctxt, DFL_VAL)
        super(DFL_VAL_FUNCTION, self).__init__(11, func, ctxt)
 

class DFL_VAL_FIXPOINT(DFL_VAL):
    def __init__(self, func: DFL_AST_NODE, ctxt: DFL_CTXT):
        assert isinstance(func, DFL_AST_NODE)
        assert isinstance(ctxt, DFL_VAL)
        super(DFL_VAL_FIXPOINT, self).__init__(12, func, ctxt)

class DFL_VAL_REFERENCE(DFL_VAL):
    def __init__(self, addr):
        assert isinstance(addr, int)
        super(DFL_VAL_REFERENCE, self).__init__(13, addr)

class DFL_VAL_CONS(DFL_VAL):    
    def __init__(self, head: DFL_VAL, tail: DFL_VAL):
        assert isinstance(head, DFL_VAL)
        assert isinstance(tail, DFL_VAL)
        super(DFL_VAL_CONS, self).__init__(14, head, tail)

class DFL_VAL_NIL(DFL_VAL):
    def __init__(self):
        super(DFL_VAL_NIL, self).__init__(15)

def test():
    var = DFL_TERM_VARIABLE(DFL_Variable.Declare("hahe"))
    term = DFL_TERM_APPLY(DFL_TERM_FUNCTION(var, DFL_TERM_OPERATION("++", var)), DFL_TERM_INT(1))
    val = DFL_VAL_PDF(pd.DataFrame({"a": [1], "b": [2]}))
    print(term, val)
    print(DFL_VAL_FUNCTION(term, val))

if __name__ == "__main__":
    test()