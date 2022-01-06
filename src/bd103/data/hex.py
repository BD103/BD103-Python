"""Provides methods and classes to translate various data types to and from the hex format.

This module is heavily based off of other data format modules, like :mod:`json` and :mod:`pickle`.

See Also:
    - `Hexadecimal on Wikipedia <https://en.wikipedia.org/wiki/Hexadecimal>`_
"""

import binascii
import typing as t
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
    """Used to turn data into a string of hexadecimals.

    Args:
        return_uppercase: Whether letters in returned hex should be capitalized.
        prefix_zero: If the returned value if only 1 character long, it will prefix the returned value with a ``0``.
        prefix_str_encoding: If true, all encoded strings will be prefixed with the encoding of the text.
        truth_value: When given a boolean, it will translate the value to a number. Default or 15, or ``f``.
        default_str_encoding: The encoding that should be preferred when encoding strings.
        string_encode_error_handler: How to treat errors when formatting a string in :meth:`encode_str`.
        string_decode_error_handler: How to treat errors when converting bytes to string in :meth:`encode_str`.

    See Also:
        - `Encode / Decode error handlers <https://docs.python.org/3/library/codecs.html#error-handlers>`_
    """

    return_uppercase: bool
    prefix_zero: bool
    prefix_str_encoding: bool
    truth_value: int
    default_str_encoding: str
    string_encode_error_handler: str
    string_decode_error_handler: str

    def __init__(
        self,
        return_uppercase: bool = False,
        prefix_zero: bool = True,
        prefix_str_encoding: bool = True,
        truth_value: int = 255,
        default_str_encoding: str = "ascii",
        string_encode_error_handler: str = "strict",
        string_decode_error_handler: str = "strict",
    ):
        self.return_uppercase = return_uppercase
        self.prefix_zero = prefix_zero
        self.prefix_str_encoding = prefix_str_encoding
        self.truth_value = truth_value
        self.default_str_encoding = default_str_encoding
        self.string_encode_error_handler = string_encode_error_handler
        self.string_decode_error_handler = string_decode_error_handler

    def encode_int(self, o: int) -> str:
        # Ensure it is integer
        if not isinstance(o, int):
            raise TypeError(f"o's type {type(o)} is not an integer")

        # Ensure that no recursion error happens when converting negative numbers
        if not o >= 0:
            raise TypeError("o cannot be converted to a hex because it is less than 0")

        return self._format_response(self._encode_int(o))

    def _encode_int(self, o: t.Union[int, float]) -> str:
        remainder = o % 16

        if o - remainder == 0:
            return hex_keys.inverse[remainder]

        # Recursively find value then add together
        return self._encode_int((o - remainder) / 16) + hex_keys.inverse[remainder]

    def encode_bool(self, o: bool) -> str:
        if o:
            return self._format_response(self.encode_int(self.truth_value))
        else:
            return self._format_response(hex_keys.inverse[0])

    def encode_str(self, o: str, str_encoding: str = None) -> list[str]:
        str_loop = self.i_encode_str(o, str_encoding)

        if self.prefix_str_encoding:
            # So the encoding doesn't get formatted
            res = [next(str_loop)]
        else:
            res = []

        res += [self._format_response(i) for i in str_loop]

        return res

    def i_encode_str(self, o: str, str_encoding: str = None) -> abc.Iterable[str]:
        _str_encoding = str_encoding or self.default_str_encoding

        if self.prefix_str_encoding:
            yield _str_encoding

        for char in o:
            yield binascii.b2a_hex(
                char.encode(_str_encoding, errors=self.string_encode_error_handler)
            ).decode(errors=self.string_decode_error_handler)

    def encode_list(self, o: list[t.Union[str, list[str]]]):
        """Encodes a list of data through :meth:`smart_encode`.

        Warning:
            Encoded strings and lists have the same data type.
            When decoding a list, make sure you configure :class:`HexDecoder` to prefer the list or string type.
            This may cause weird errors in your code, so it is recommended to only encode simple data types.
        """
        return [self.smart_encode(i) for i in o]

    def _format_response(self, o: str) -> str:
        res = o

        if self.return_uppercase:
            res = res.upper()
        else:
            res = res.lower()

        if self.prefix_zero and len(res) == 1:
            res = "0" + res

        return res

    def smart_encode(self, o: t.Any) -> t.Union[str, list[str]]:
        if isinstance(o, bool):
            return self.encode_bool(o)
        elif isinstance(o, int):
            return self.encode_int(o)
        elif isinstance(o, str):
            return self.encode_str(o)
        elif isinstance(o, list):
            return self.encode_list(o)
        else:
            raise TypeError(
                f"Given data {repr(o)}'s type is not supported by HexEncoder"
            )


class HexDecoder(object):
    def __init__(self):
        pass


_default_encoder = HexEncoder()
_default_decoder = HexDecoder()


def dumps(o: t.Any, **kwargs) -> t.Union[str, list[str]]:
    """Converts an integer or list of integers into a string.

    Args:
        o: An integer or list of integers to be encoded.
        **kwargs: Arguments to be passed on initialization of a new instance of :class:`HexEncoder`.
    """

    if not kwargs:
        encoder = _default_encoder
    else:
        encoder = HexEncoder(**kwargs)

    return encoder.smart_encode(o)


def loads(o: str, **kwargs):
    """Converts a hexadecimal string to an integer or list of integers.

    Args:
        o: A hexadecimal string to be decoded.
        **kwargs: Arguments to be passed on initialization of a new instance of :class:`HexDecoder`.
    """
    if not kwargs:
        decoder = _default_decoder
    else:
        decoder = HexDecoder(**kwargs)

    # Just a placeholder
    print(decoder)
