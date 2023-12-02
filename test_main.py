"""
Test goes here

"""

from mylib.__init__ import add


def test_add():
    assert add(1, 2) == 3
    assert add(3, 2) == 5
    assert add(10, 12) == 22
