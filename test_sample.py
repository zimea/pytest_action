import pytest

def func(x):
    return x + 2

def test_success():
    assert func(3) == 5

def test_success():
    assert func(32) == 5