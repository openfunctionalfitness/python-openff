from openff.transform import (
    parse_cap, parse_time
)


def test_cap():
    assert parse_cap("CAP +36") == 36.0
    assert parse_cap("CAP+41") == 41.0
    assert parse_cap("CAP+ 54") == 54.0


def test_time():
    assert parse_time("1:15:59") == 60 * 60 + 15 * 60 + 59
    assert parse_time("24:31.18") == 24 * 60 + 31 + .18
    assert parse_time("02:52") == 2 * 60 + 52

def extrap_cap2sec():
    sec = extrap_cap2sec("cap +123", 10, 200)
    assert sec / (10*60) == 200 / 123
