"""SFP - Simple Functional Programming."""
from functools import reduce, wraps


def tail(iterable):
    """Get tail of a iterable is everything except the first element."""
    r = [x for x in iterable]
    return r[1:]


def pipe(*args):
    """All the arguments given to this function will be passed as param to
    `reduce` and it will return a function with all closures set to pipe in."""
    return reduce(_pipe, args)


def _pipe(curr, prev):
    """Callback to `reduce` function."""
    return lambda x: prev(curr(x))


def zipwith(func: callable) -> callable:
    """
    Zipwith concat two sequences using a function.

    >>> zipwith(lambda x: x + y)([1,2,3], [4,5,6])
    """
    @wraps(func)
    def inner(sequence_a: iter, sequence_b: iter) -> iter:
        for el_a, el_b in zip(sequence_a, sequence_b):
            yield func(el_a, el_b)
    return inner
