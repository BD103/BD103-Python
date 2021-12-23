"""Provides methods and classes to translate various data types to and from the hex format.

This module is heavily based off of other data format modules, like :mod:`json` and :mod:`pickle`.

See Also:
    - `Hexadecimal on Wikipedia <https://en.wikipedia.org/wiki/Hexadecimal>`_
"""

import binascii
from collections import abc

from bidict import bidict

hex_keys: bidict[str, int] = bidict(
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
    """Used to turn data into a string of hexedecimals.

    Args:
        return_uppercase: Whether letters in returned hex should be capitalized. Default is false, uncapitalized.
        prefix_zero: If the returned value if only 1 character long, it will prefix the returned value with a ``0``.
        prefix_str_encoding: If true, all encoded strings will be prefixed with the encoding of the text.
        truth_value: When given a boolean, it will translate the value to a number. Default or 15, or ``f``.
    """

    return_uppercase: bool = False
    prefix_zero: bool = True
    prefix_str_encoding: bool = True
    truth_value: int = 15
    default_str_encoding: str = "ascii"

    def __init__(self, return_uppercase: bool = None, truth_value: int = None):
        self.return_uppercase = return_uppercase or self.return_uppercase
        self.truth_value = truth_value or self.truth_value

    def encode_int(self, o: int) -> str:
        # Ensure it is integer
        if not isinstance(o, int):
            raise TypeError(f"o's type {type(o)} is not an integer")

        # Ensure that no recursion error happens when converting negative numbers
        if not o >= 0:
            raise TypeError("o cannot be converted to a hex because it is less than 0")

        return self._format_response(self._encode_int(o))

    def _encode_int(self, o: int) -> str:
        remainder = o % 16

        if o - remainder == 0:
            return hex_keys.inverse[remainder]

        # Recursively find value then add together
        return self._encode_int((o - remainder) / 16) + hex_keys.inverse[remainder]

    def encode_bool(self, o: bool) -> str:
        if o:
            return self._format_response(hex_keys.inverse[self.truth_value])
        else:
            return self._format_response(hex_keys.inverse[0])

    def encode_str(self, o: str, str_encoding: str = None) -> list[str]:
        return list(self.i_encode_str(o, str_encoding=str_encoding))

    def i_encode_str(self, o: str, str_encoding: str = None) -> abc.Iterable:
        _str_encoding = str_encoding or self.default_str_encoding

        if self.prefix_str_encoding:
            yield _str_encoding

        for char in o:
            yield binascii.b2a_hex(char.encode(_str_encoding))

    def _format_response(self, o: str) -> str:
        res = o

        if self.return_uppercase:
            res = res.upper()
        else:
            res = res.lower()

        if self.prefix_zero and len(res) == 1:
            res = "0" + res

        return res


class HexDecoder(object):
    def __init__(self):
        pass


_default_encoder = HexEncoder()
_default_decoder = HexDecoder()


def dumps(o: int, **kwargs) -> str:
    """Converts an integer or list of integers into a string.

    Args:
        o: An integer or list of integers to be encoded.
        **kwargs: Arguments to be passed on initialization of a new instance of :class:`HexEncoder`.
    """

    if not kwargs:
        encoder = _default_encoder
    else:
        encoder = HexEncoder(**kwargs)

    if isinstance(o, int):
        return encoder.encode_int(o)


def loads(o: str, **kwargs) -> int:
    """Converts a hexedecimal string to an integer or list of integers.

    Args:
        o: A hexedecimal string to be decoded.
        **kwargs: Arguments to be passed on initialization of a new instance of :class:`HexDecoder`.
    """
    if not kwargs:
        decoder = _default_decoder
    else:
        decoder = HexDecoder(**kwargs)

    # Just a placeholder
    print(decoder)


if __name__ == "__main__":
    pass
