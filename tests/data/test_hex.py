import pytest

# from bd103.data import hex


@pytest.mark.skip(reason="No hex module for now")
class TestHexEncoder(object):
    def test_defaults(self):
        encoder = hex.HexEncoder()

        # Integer
        assert encoder.encode_int(0) == "00"
        assert encoder.encode_int(208) == "d0"
        assert encoder.encode_int(255) == "ff"

        # Bool
        assert encoder.encode_bool(True) == "ff"
        assert encoder.encode_bool(False) == "00"

        # String
        assert encoder.encode_str("{bd103}") == [
            "ascii",
            "7b",
            "62",
            "64",
            "31",
            "30",
            "33",
            "7d",
        ]
        assert encoder.encode_str("{bd103}", "utf-8") == [
            "utf-8",
            "7b",
            "62",
            "64",
            "31",
            "30",
            "33",
            "7d",
        ]
        assert encoder.encode_str("{bd103}", "utf-16") == [
            "utf-16",
            "fffe7b00",
            "fffe6200",
            "fffe6400",
            "fffe3100",
            "fffe3000",
            "fffe3300",
            "fffe7d00",
        ]
