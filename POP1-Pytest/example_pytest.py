import pytest


def add5(x):
    my_val = x + 5
    return my_val


def test_add5():
    assert add5(1) == 6
    assert add5(3) == 8
    assert add5(1) == 5
