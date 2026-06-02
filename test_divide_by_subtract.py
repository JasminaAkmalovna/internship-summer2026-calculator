import pytest
from divide import divide


def test_divide_positive():
    assert divide(10, 2) == 5


def test_divide_decimal():
    assert divide(5, 2) == 2.5


def test_divide_negative():
    assert divide(-10, 2) == -5


def test_divide_zero_by_number():
    assert divide(0, 5) == 0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_divide_string():
    with pytest.raises(TypeError):
        divide("10", 2)