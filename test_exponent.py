import pytest
from exponent import exponent


def test_exponent_positive():
    assert exponent(2, 3) == 8


def test_exponent_zero_power():
    assert exponent(5, 0) == 1


def test_exponent_one_power():
    assert exponent(7, 1) == 7


def test_exponent_zero_base():
    assert exponent(0, 5) == 0