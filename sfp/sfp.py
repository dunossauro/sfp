"""SFP - Simple Functional Programming."""
from functools import reduce


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


def compose(*args):
    """Composes all the given function in one."""
    return reduce(lambda fun, tion: lambda arg: fun(tion(arg)),
                  args,
                  lambda arg: arg)
