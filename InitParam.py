from types import FunctionType, GenericAlias
import inspect

class init(type):
    def __new__(metacls, name, parents, ns, **kwds):
        return super().__new__(metacls, name, parents, ns)

    def __init__(cls, name, parents, ns, **kwds):
        for attr_name, attr in vars(cls).items():
            if isinstance(attr, FunctionType):
                defaults = []
                for arg in inspect.signature(attr).parameters.values():
                    if arg.default == inspect.Parameter.empty:
                        argdefault_type = arg.annotation.__origin__() if issubclass(arg.annotation, GenericAlias) \
                            else arg.annotation
                        try:
                            argdefault = argdefault_type()
                        except Exception:
                            argdefault = None
                    else:
                        argdefault = arg.default
                    defaults.append(argdefault)
                attr.__defaults__ = tuple(defaults)

        super().__init__(name, parents, ns)
