#!/bin/python3

from math_utils import add,sub,div
import pytest

def test_add():
    assert add(2,1) == 3

def test_sub():
    assert sub(10,7) == 3

def test_divide():
    assert div(9,3) == 3

def test_divide_byZero():
    with pytest.raises(ValueError):
         div(10,0)


