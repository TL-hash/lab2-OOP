import pytest
from tasks.task1 import Diapason, make_diapason

def test_diapason_creation():
    d = Diapason(1.5, 3.7)
    assert d.first == 1.5
    assert d.second == 3.7

def test_diapason_invalid_creation():
    with pytest.raises(ValueError):
        Diapason("abc", 3.7)
    with pytest.raises(ValueError):
        Diapason(5.0, 2.0)

def test_rangecheck():
    d = Diapason(1.5, 3.7)
    assert d.rangecheck(2.0) is True
    assert d.rangecheck(1.5) is True
    assert d.rangecheck(3.7) is True
    assert d.rangecheck(1.0) is False
    assert d.rangecheck(4.0) is False

def test_make_diapason():
    d = make_diapason(0.0, 10.0)
    assert d.first == 0.0
    assert d.second == 10.0
    with pytest.raises(ValueError):
        make_diapason(10.0, 0.0)