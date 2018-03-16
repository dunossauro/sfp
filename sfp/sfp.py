"""SFP - Simple Functional Programming."""
from functools import reduce


def tail(iterable):
    """Get tail of a iterable is everything except the first element."""
    r = [x for x in iterable]
    return r[1:]


def pipe(*args):
    """ NOTE: insert documentation."""
    return reduce(_pipe, args)


def _pipe(prev, curr):
    """ NOTE: insert documentation."""
    return lambda x: prev(curr(x))
