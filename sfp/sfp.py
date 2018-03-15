"""SFP - Simple Functional Programming."""


def tail(iterable):
    """Get tail of a iterable is everything except the first element."""
    r = [x for x in iterable]
    return r[1:]