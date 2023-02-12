import numbers
import types
from fractions import Fraction
from decimal import Decimal


class fixed(type):
    #@classmethod
    #def __prepare__(metacls, name, bases, ndigits=3, *args, **kwds):
    #    print(f'{metacls=}')
    #    metacls.ndigits = ndigits
    #    print(f'{ndigits=}')
    #    print("prepare", name, bases, kwds)
    #    return super().__prepare__(name, bases, **kwds)

    @staticmethod
    def __new__(metacls, name, parents, ns, **kwds):
        ndigits = kwds['ndigits']
        new_ns = {key: f(key, val, ndigits) if isinstance(val, types.FunctionType) else val for key, val in ns.items()}

        print(f'{new_ns=}')

        return super().__new__(metacls, name, parents, new_ns)

    @staticmethod
    def new_func(func):
        def f(self, *args, **kwargs):
            print(f'{args=} {kwargs=}')
            print(len(args))
            res = func(args, kwargs)
            if res is numbers.Real:
                return round(res, ndigits=fixed.ndigits)
            else:
                return res

        return f


def f(name, func, ndigits=3):
    def new_func(self, *args, **kwargs):
        print(f'f new_func {self=}')
        print(f'{name=} {args=} {kwargs=}')
        res = 5.15464545
        res = eval(f'self.{name}(args, kwargs)')
        if isinstance(res, numbers.Real):
            return round(res, ndigits=ndigits)
        else:
            return res
    return new_func

class C(metaclass=fixed, ndigits=4):
    def div(self, a, b):
        print(f'{self=} {a=} {b=}')
        return a / b

c = C()
c.div(6, 7)
print(C().div(6, 7))
print(C().div(Fraction(6), Fraction(7)))
print(C().div(Decimal(6), Decimal(7)))