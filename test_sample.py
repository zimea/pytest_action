import pytest

def func(x):
    return x + 2

def func2(x):
    return x + 3

def test_success():
    assert func(3) == 5

def test_success():
    assert func2(2) == 5