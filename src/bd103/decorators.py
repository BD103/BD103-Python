"""Contains useful decorators that can be applied to various objects (usually functions).

One of the most common variants of decorators are prefixed with ``requires_``. They only allow the function to run if a specific requirement is met.
"""

import functools
import importlib.util
import platform
import typing as t
from collections import abc


def requires_os(
    os_name: t.Union[str, t.List[str]], silent: bool = False
) -> abc.Callable:
    """Only allows the use of the function if running on a certain operating system.

    OS detection is done through :func:`platform.system()`.

    Args:
        os_name: A string or list of strings that say either "windows", "ubuntu", or "darwin". (Or anything that :func:`platform.system()` might return.)
        silent: If false and on the wrong OS, it will raise an :exc:`OSError`. If true, it will skip the function and continue.

    Examples:
        .. code-block:: python

            @requires_os("windows")
            def only_windows():
                print("I CAN SEE THROUGH WINDOWS")

        .. code-block:: python

            @requires_os(["linux", "darwin"])
            def access_home() -> str:
                with open("~/myfile.txt", "rt") as fp:
                    return fp.read()

    Raises:
        OSError: Wrong OS type!
    """

    def decorator(func: abc.Callable) -> abc.Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if isinstance(os_name, str):
                if platform.system().lower() == os_name.lower():
                    return func(*args, **kwargs)
                elif not silent:
                    raise OSError(f"OS {platform.system()} does not equal {os_name}")
            elif isinstance(os_name, list):
                if platform.system().lower() in [i.lower() for i in os_name]:
                    return func(*args, **kwargs)
                elif not silent:
                    raise OSError(f"OS {platform.system()} is not in {os_name}")
            else:
                raise TypeError(f"os_name type {type(os_name)} is not string or list")

        return wrapper

    return decorator


def requires_module(
    module: str, package: str = None, silent: bool = False
) -> abc.Callable:
    """Only allows the use of the function if a certain module or package is installed.

    This uses :mod:`importlib` to detect what modules are installed. A common example of this decorator would be in the :mod:`bd103.ext` package.

    Args:
        module: The name of the module that needs to be installed. This also works on subpackages.
        package: Finds module relative to the given package name. See :func:`importlib.util.find_spec`.
        silent: If false, this function will raise a :exc:`ModuleNotFoundError`. If true, it will skip this function and continue.

    Examples:
        .. code-block:: python

            try:
                import colorama
            except ImportError:
                colorama = None

            @requires_module("colorama")
            def do_color_stuff():
                colorama.init()
                print("\\x1b[34mHELLO\\x1b[0m")
                colorama.deinit()

    Raises:
        ModuleNotFoundError: Package is most likely not installed.
    """

    def decorator(func: abc.Callable) -> abc.Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if importlib.util.find_spec(module, package=package):
                return func(*args, **kwargs)
            elif not silent:
                if package is None:
                    raise ModuleNotFoundError(
                        f"{repr(func)} requires module {module} to run"
                    )
                else:
                    raise ModuleNotFoundError(
                        f"{repr(func)} requires module {module} from package {package} to run"
                    )

        return wrapper

    return decorator
