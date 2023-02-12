def maxfun(s, *funcs):
    maxfun = funcs[0]
    maxsum = sum([maxfun(_) for _ in s])
    for func in funcs:
        if (cursum := sum([func(_) for _ in s])) >= maxsum:
            maxfun = func
            maxsum = cursum

    return maxfun
