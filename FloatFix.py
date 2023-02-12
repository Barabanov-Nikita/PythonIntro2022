import numbers
from functools import wraps
from types import FunctionType


def fix(fun, ndigits):
    @wraps(fun)
    def nfun(*args, **kwargs):
        ret = fun(*args, **kwargs)
        return round(ret, ndigits) if isinstance(ret, numbers.Real) else ret
    return nfun


class fixed(type):
    def __new__(metacls, name, parents, ns, **kwds):
        return super().__new__(metacls, name, parents, ns)

    def __init__(cls, name, parents, ns, **kwds):
        ndigits = kwds.get("ndigits", 3)
        for attr_name, attr in vars(cls).items():
            if isinstance(attr, FunctionType):
                setattr(cls, attr_name, fix(attr, ndigits))
        super().__init__(name, parents, ns)
