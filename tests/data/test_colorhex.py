import pytest

from bd103.data import ColorHex


@pytest.fixture
def hex_class():
    return ColorHex("#")
