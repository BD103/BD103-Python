from bd103.data import hex


class TestDumps(object):
    def test_normal(self):
        assert hex.dumps(0) == "00"
        assert hex.dumps(15) == "0f"
        assert hex.dumps(16) == "10"
        assert hex.dumps(32) == "20"
        assert hex.dumps(78) == "4e"
        assert hex.dumps(255) == "ff"


def test_dumps():
    assert hex._default_encoder.encode_int(256) == "100"
