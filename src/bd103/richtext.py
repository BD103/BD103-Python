"""Does some fun assorted things with ANSI color codes.

This module originally came from a small project called Dogelib. That project is now archived, but the code lives on.

See Also:
    - `Dogelib <https://github.com/BD103/Dogelib>`_
"""

from collections import abc
from random import randint

_colors: dict[str, list[int]] = {
    "basic": [31, 33, 32, 36, 34, 35],
    "bg": [41, 43, 42, 46, 44, 45],
    "ex": [91, 93, 92, 96, 94, 95],
    "bgex": [101, 103, 102, 106, 104, 105],
}


def _rainbow_iter(palette: str = "basic") -> abc.Generator[int, None, None]:
    while True:
        for i in _colors[palette]:
            yield i


def make_rainbow(text: str, palette: str = "basic") -> str:
    res = ""
    rotation = _rainbow_iter(palette)

    for i in text:
        res += f"\x1b[{next(rotation)}m{i}"

    rotation.close()
    res += "\x1b[0m"

    return res


def make_colorful(text: str, palette: str = "basic") -> str:
    return "\x1b[{0}m{1}\x1b[0m".format(
        _colors[palette][randint(0, len(_colors[palette]) - 1)], text
    )


if __name__ == "__main__":
    print(make_rainbow("This is some colorful text :)", "ex"))
    print(make_colorful("This randomly is a different color"))
