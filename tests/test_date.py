import pytest
from tasks.task2 import Date, make_date


def test_date_creation():
    d1 = Date(2004, 8, 31)
    assert d1.year == 2004 and d1.month == 8 and d1.day == 31

    d2 = Date("2004.02.29")
    assert d2.year == 2004 and d2.month == 2 and d2.day == 29

    d3 = Date(d1)
    assert d3.year == 2004 and d3.month == 8 and d3.day == 31

    with pytest.raises(ValueError):
        Date(2004, 2, 30)


def test_is_leap():
    assert Date(2000, 1, 1).is_leap() is True
    assert Date(1900, 1, 1).is_leap() is False
    assert Date(2004, 1, 1).is_leap() is True
    assert Date(2003, 1, 1).is_leap() is False


def test_add_sub_days():
    d = Date(2004, 2, 28)
    assert d.add_days(1).equals(Date(2004, 2, 29))
    assert d.add_days(2).equals(Date(2004, 3, 1))

    d_ny = Date(2004, 12, 31)
    assert d_ny.add_days(1).equals(Date(2005, 1, 1))

    d_march = Date(2004, 3, 1)
    assert d_march.sub_days(1).equals(Date(2004, 2, 29))


def test_comparisons():
    d1 = Date(2004, 8, 31)
    d2 = Date(2004, 8, 31)
    d3 = Date(2004, 8, 30)

    assert d1.equals(d2) is True
    assert d1.equals(d3) is False

    assert d1.before(d3) is False
    assert d3.before(d1) is True

    assert d1.after(d3) is True
    assert d3.after(d1) is False