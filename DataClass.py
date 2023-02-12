def sloter(fields, default):
    class SlotClass:
        __slots__ = list(fields)

        def __init__(self):
            for slot in self.__slots__:
                self.__setattr__(slot, default)

        def __delattr__(self, item):
            if item in self.__slots__:
                self.__setattr__(item, default)
            else:
                raise AttributeError

        def __iter__(self):
            return iter(getattr(self, slot) for slot in self.__slots__)

    return SlotClass
