from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([1, 2, 3], -10) == [1, 2, 3]

def test_get_val():
    assert arrs.get_val({}, 'vsc') == 'git'
    assert arrs.get_val({}, 'vsc', 'cat') == 'cat'
    assert arrs.get_val({1: 'forest'}, 1) == 'forest'
    assert arrs.get_val({1: 'forest'}, 2) == 'git'
    assert arrs.get_val({1: 'forest'}, 2, 'cat') == 'cat'
