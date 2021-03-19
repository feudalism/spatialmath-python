
# _numba = True
from functools import wraps
import os

try:
    global _numba
    import numba
    _numba = True
except ImportError:
    # global _numba
    _numba = False


# Equivalent to @numba.njit
def numba_njit(func):
    if _numba:
        return (numba.njit(cache=True))(func)
    else:
        return func

    # @wraps(func)
    # def wrapper(*args, **kwargs):
    #     if _numba:
    #         return junc(*args, **kwargs)
    #     else:
    #         return func(*args, **kwargs)

    # return wrapper


# Equivalent to @numba.extending.overload(method)
def numba_overload(method):
    def decor(func):
        if _numba:
            return (numba.extending.overload(method))(func)
        else:
            return func
    
    return decor


def use_numba(use_numba):
    global _numba
    _numba = use_numba


def using_numba():
    global _numba
    return _numba
