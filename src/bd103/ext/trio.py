"""Extensions to the :mod:`trio` package.

The Trio library contains an easy API for asynchronous Python programs. Most objects in this extension module will require asynchronous syntax, like ``async`` and ``await``.

Note:
    You can install :mod:`trio` with:

    .. code-block:: shell

        python -m pip install -U trio"""


import functools
from collections import abc

from bd103.decorators import requires_module

try:
    import trio
except ImportError:
    trio = None


@requires_module("trio")
def run_wrapper() -> abc.Callable:
    """Allows an asynchronous function to be called from synchronous code.

    This works by wrapping the function in :func:`trio.run`. Note that certain keyword arguments may cause unwanted effects because they are intercepted by :func:`trio.run`.

    Example:
        .. code-block:: python

            @run_wrapper()
            async def do_thing():
                print("Hello!")
                await trio.sleep(3)
                print("Goodbye!")

            # Instead of trio.run(do_thing)
            do_thing()

    Raises:
        ModuleNotFoundError: If :mod:`trio` is not installed, you will not be able to apply this decorator."""

    def decorator(func: abc.Callable) -> abc.Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            trio.run(func, *args, **kwargs)

        return wrapper

    return decorator
