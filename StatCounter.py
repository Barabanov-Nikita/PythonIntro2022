def statcounter():
    stats = {}
    f = (yield stats)
    while True:
        stats.setdefault(f, 0)
        def tmp(*args, f=f):
            stats[f] += 1
            return f(*args)
        f = (yield tmp)
