import enum
import abc
from dfl_type import *

 

class DFL_Variable:
    _stamp_stk = tuple((0, ))
     
    def Declare(name = "", type = DFL_TYPE_EXIST(DFL_TYPEVAR.new())):
        top_stamp = DFL_Variable._stamp_stk[0]
        DFL_Variable._stamp_stk = tuple((top_stamp + 1, DFL_Variable._stamp_stk)) 
        return DFL_Variable(name, type, top_stamp)
    
    def __init__(self, name, type, stamp):
        self._name = name
        self._type = type
        self._stamp = stamp

    @property
    def name(self):
        return self._name
    @property
    def type(self):
        return self._type
    @property
    def stamp(self):
        return self._stamp
    @name.setter
    def name(self, *args, **kwargs):
        raise NotImplementedError
    @type.setter
    def type(self, *args, **kwargs):
        raise NotImplementedError
    @stamp.setter
    def stamp(self, *args, **kwargs):
        raise NotImplementedError

    def __eq__(self, other):
        return self.stamp == other.stamp
    


def test_Variable():
    var1 = DFL_Variable.Declare("hehe")
    var2 = DFL_Variable.Declare("haha")
    print(var1.stamp, var2.stamp, DFL_Variable._stamp_stk)

if __name__ == "__main__":
    test_Variable()