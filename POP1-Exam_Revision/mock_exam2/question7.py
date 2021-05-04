# 13198061

class My_integer:
    def __init__(self, x):
        # method creates My_integer object that represents
        # a usual Python integer x
        self._x = x

    def increase(self, o):
        # method increases the value of this object by the
        # value represented by another My_integer object o;
        # method returns nothing
        self._x += o._x

    def plus(self, o):
        # method returns the My_integer object representing
        # the sum of the value represented by this object and
        # the value represented by My_integer object o
        return My_integer(self._x + o._x)
    
        # return self._x + o._x

    def __eq__(self, other):
        if self._x == other:
            return True
        return False
    
"""
    def __eq__(self, o):
        return self._x == o._x

    def __ne__(self, o):
        return self._x != o._x
"""        
