"""
Found on `https://stackoverflow.com/questions/3888158/making-decorators-with-optional-arguments`
"""

import functools
def decorator(original_function=None, optional_argument1=None, optional_argument2=None, ...):

    def _decorate(function):

        @functools.wraps(function)
        def wrapped_function(*args, **kwargs):
            ...

        return wrapped_function

    if original_function:
        return _decorate(original_function)

    return _decorate
