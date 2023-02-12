class Nuts:
    def __init__(self, *args):
        pass

    def __getitem__(self, item):
        return item

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __getattr__(self, item):
        return item

    def __delattr__(self, item):
        pass

    def __setattr__(self, key, value):
        pass

    def __iter__(self):
        return iter("Nuts")

    def __str__(self):
        return "Nuts"

