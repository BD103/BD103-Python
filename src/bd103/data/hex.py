"""Provides methods and classes to translate various data types to and from the hex format.

This module is heavily based off of other data format modules, like :mod:`json` and :mod:`pickle`.

See Also:
    - `Hexadecimal on Wikipedia <https://en.wikipedia.org/wiki/Hexadecimal>`_
"""

from bidict import bidict

int_keys: bidict[str, int] = bidict(
    {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15,
    }
)


class HexEncoder(object):
    def __init__(self):
        pass

    def encode_int(self, o: int) -> str:
        remainder = o % 16

        if o - remainder == 0:
            return int_keys.inverse[remainder]

        return self.encode_int((o - remainder) / 16) + int_keys.inverse[remainder]

    def encode_list(self, o: list[str]) -> str:
        res = ""

        for i in o:
            res += self.encode_int(i)

        return res


class HexDecoder(object):
    list_item_len: int = 2

    def __init__(self, list_item_len: int = None):
        self.list_item_len = list_item_len or self.list_item_len

    def decode_int(self, o: str) -> int:
        """Decodes a hex string into one integer.

        This function converts each character then multiplies it by 16 if there is another character after it.
        """

        res = int_keys[o[0]]

        if len(o) == 1:
            return res

        for i in o[1:]:
            res *= 16
            res += int_keys[i]

        return res

    def decode_list(self, o: str) -> list[str]:
        req = [
            o[i : i + self.list_item_len] for i in range(0, len(o), self.list_item_len)
        ]
        res = []

        for i in req:
            res.append(self.decode_int(i))

        return res


_default_encoder = HexEncoder()
_default_decoder = HexDecoder()


def dumps(o: list[int], **kwargs) -> str:
    if not kwargs:
        return _default_encoder.encode_list(o)
    else:
        return HexEncoder(**kwargs).decode_list(o)


def loads(o: str, **kwargs) -> list[int]:
    if not kwargs:
        return _default_decoder.encode_list(o)
    else:
        return HexDecoder(**kwargs).encode_list(o)


if __name__ == "__main__":
    print(_default_decoder.decode_list("ffee"))
    # [255, 238]
    print(_default_encoder.encode_list([255, 238]))
    # "ffee"
