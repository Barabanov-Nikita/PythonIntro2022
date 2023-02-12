class NegExt:
    def __neg__(self):
        try:
            return self.__class__(super().__neg__())
        except Exception:
            try:
                return self.__class__(super().__getitem__(slice(1, -1)))
            except Exception:
                return self.__class__(self)

