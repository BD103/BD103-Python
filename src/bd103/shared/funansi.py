# From Dogelib.much
# https://github.com/BD103/Dogelib

from random import randint

_colors = {
    "basic": [31, 33, 32, 36, 34, 35],
    "bg": [41, 43, 42, 46, 44, 45],
    "ex": [91, 93, 92, 96, 94, 95],
    "bgex": [101, 103, 102, 106, 104, 105],
}


def _rainbow_iter(palette="basic"):
    while True:
        for i in _colors[palette]:
            yield i


def make_rainbow(text: str, palette="basic") -> str:
    res = ""
    rotation = _rainbow_iter(palette)

    for i in text:
        res += f"\u001b[{next(rotation)}m{i}"

    rotation.close()
    res += "\u001b[0m"

    return res


def make_colorful(text: str, palette="basic"):
    return "\u001b[{0}m{1}\u001b[0m".format(
        _colors[palette][randint(0, len(_colors[palette]) - 1)],
        text
    )


if __name__ == "__main__":
    print(make_rainbow("This is some colorful text :)", "ex"))
    print(make_colorful("This randomly is a different color"))
