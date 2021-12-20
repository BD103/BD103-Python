"""Provides methods and classes to translate various data types to and from the hex format.

This module is heavily based off of other data format modules, like :mod:`json` and :mod:`pickle`.

See Also:
    - `Hexadecimal on Wikipedia <https://en.wikipedia.org/wiki/Hexadecimal>`_
"""

import typing as t

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
    """Used to turn an integer or list of integers into a string of hexedecimals."""

    def __init__(self):
        pass

    def encode_int(self, o: int) -> str:
        """Encodes an integer into its hexedecimal equivelant.

        Args:
            o: An integer to be encoded into a hexedecimal.
        """
        remainder = o % 16

        if o - remainder == 0:
            return int_keys.inverse[remainder]

        return self.encode_int((o - remainder) / 16) + int_keys.inverse[remainder]

    def encode_list(self, o: list[int]) -> str:
        """Encodes a list of integers into one string.

        Args:
            o: A list of integers to be encoded.

        Note:
            Make sure you know the maximum size of each integer. If you wish to decode the values again, you will need to determine the value of :attr:`HexDecoder.list_item_len`. If any integer is greater than 15, it will have to have a chunk size of 2. Greater than 255 deems a chunk size of 3.
        """
        res = ""

        for i in o:
            res += self.encode_int(i)

        return res


class HexDecoder(object):
    """Used for turning a string of hexedecimals into an integer or list of integers.

    Args:
        list_item_len: The size of each chunk of data used in :meth:`decode_list`."""

    list_item_len: int = 2

    def __init__(self, list_item_len: int = None):
        self.list_item_len = list_item_len or self.list_item_len

    def decode_int(self, o: str) -> int:
        """Decodes a hex string into one integer.

        This function converts each character then multiplies it by 16 if there is another character after it.

        Args:
            o: A string to be converted into an integer. Some examples are ``ff``, ``e8``, or ``00``.

        Note:
            This method even decodes uncommon forms of hexedecimal, which means that any string you give has a chance of being larger than 255. If you want to limit the maximum value, take a look at :meth:`decode_list`.
        """

        res = int_keys[o[0]]

        if len(o) == 1:
            return res

        for i in o[1:]:
            res *= 16
            res += int_keys[i]

        return res

    def decode_list(self, o: str) -> list[int]:
        """Decodes a hex string into a list of integers.

        The size of each integer returned is determined by :attr:`list_item_len`. If it is equal to 2, then :meth:`decode_list` would parse ``fe3a`` as ``[254, 58]``.

        Args:
            o: A valid hexedecimal string."""

        req = [
            o[i : i + self.list_item_len] for i in range(0, len(o), self.list_item_len)
        ]
        res = []

        for i in req:
            res.append(self.decode_int(i))

        return res


_default_encoder = HexEncoder()
_default_decoder = HexDecoder()


def dumps(o: t.Union[list[int], int], **kwargs) -> str:
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
    elif isinstance(o, list):
        return encoder.encode_list(o)


def loads(o: str, return_list: bool = True, **kwargs) -> list[int]:
    """Converts a hexedecimal string to an integer or list of integers.

    Args:
        o: A hexedecimal string to be decoded.
        return_list: Whether to return a list of integers or one combined integer.
        **kwargs: Arguments to be passed on initialization of a new instance of :class:`HexDecoder`.
    """
    if not kwargs:
        decoder = _default_decoder
    else:
        decoder = HexDecoder(**kwargs)

    if return_list:
        return decoder.decode_list(o)
    else:
        return decoder.decode_int(o)


if __name__ == "__main__":
    print(dumps([16]))
