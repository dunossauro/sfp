"""SFP - Simple Functional Programming."""


def tail(iterable):
    """Get tail of a iterable is everything except the first element."""
    r = [x for x in iterable]
    return r[1:]


def head(iterable: iter, n: int=1) -> iter:
    """Get head of an iterable is the upper part of iterable."""
    return iterable[:n]
