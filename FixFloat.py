def fix(n):
    def dec(f):
        def newf(*args, **kwargs):
            rounder = lambda x: round(x, n) if isinstance(x, float) else x
            args = map(rounder, args)
            kwargs = {key: rounder(val) for key, val in kwargs.items()}
            return rounder(f(*args, **kwargs))
        return newf
    return dec
