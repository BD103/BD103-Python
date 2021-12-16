from bd103.richtext import make_rainbow, make_colorful, _colors
import pytest


class TestMakeRainbow(object):
    test_input = "hello"

    def test_basic(self):
        test_output = "\x1b[31mh\x1b[33me\x1b[32ml\x1b[36ml\x1b[34mo\x1b[0m"

        assert make_rainbow(TestMakeRainbow.test_input, "basic") == test_output

    def test_bg(self):
        test_output = "\x1b[41mh\x1b[43me\x1b[42ml\x1b[46ml\x1b[44mo\x1b[0m"

        assert make_rainbow(TestMakeRainbow.test_input, "bg") == test_output

    def test_ex(self):
        test_output = "\x1b[91mh\x1b[93me\x1b[92ml\x1b[96ml\x1b[94mo\x1b[0m"

        assert make_rainbow(TestMakeRainbow.test_input, "ex") == test_output

    def test_bgex(self):
        test_output = "\x1b[101mh\x1b[103me\x1b[102ml\x1b[106ml\x1b[104mo\x1b[0m"

        assert make_rainbow(TestMakeRainbow.test_input, "bgex") == test_output


# The one problem with this test is that you can never
# be positive whether a test passed or you were just
# lucky because of the random number generator :I
class TestMakeColorful(object):
    test_input = "I am very colorful"

    def test_basic(self):
        test_output = [f"\x1b[{i}mI am very colorful\x1b[0m" for i in _colors["basic"]]

        assert make_colorful(TestMakeColorful.test_input, "basic") in test_output

    def test_bg(self):
        test_output = [f"\x1b[{i}mI am very colorful\x1b[0m" for i in _colors["bg"]]

        assert make_colorful(TestMakeColorful.test_input, "bg") in test_output
    
    def test_ex(self):
        test_output = [f"\x1b[{i}mI am very colorful\x1b[0m" for i in _colors["ex"]]

        assert make_colorful(TestMakeColorful.test_input, "ex") in test_output
    
    def test_bgex(self):
        test_output = [f"\x1b[{i}mI am very colorful\x1b[0m" for i in _colors["bgex"]]

        assert make_colorful(TestMakeColorful.test_input, "bgex") in test_output
