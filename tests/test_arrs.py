import pytest
from utils import arrs

@pytest.fixture
def coll_1():
    return {1: 'forest'}

def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([1, 2, 3], -10) == [1, 2, 3]


def test_get_val(coll_1):

    assert arrs.get_val(coll_1, 1) == 'forest'
    assert arrs.get_val(coll_1, 2) == 'git'
    assert arrs.get_val(coll_1, 2, 'cat') == 'cat'

def test_get_val_empty():
    assert arrs.get_val({}, 'vsc') == 'git'
    assert arrs.get_val({}, 'vsc', 'cat') == 'cat'
