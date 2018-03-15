from functools import reduce

def pipe(*args):
    return reduce(_pipe, args)

def _pipe(prev, curr):
    return lambda x: prev(curr(x))
