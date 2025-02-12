import pytest
from solution import my_sum


def test_my_sum_empty():
    assert my_sum() == 0, "Empty input should return 0"


def test_my_sum_positive_integers():
    assert my_sum(1, 2, 3) == 6, "Should correctly sum positive integers"


def test_my_sum_negative_integers():
    assert my_sum(-1, -2, -3) == -6, "Should correctly sum negative integers"


def test_my_sum_mixed_integers():
    assert my_sum(-1, 1, -2, 2, 30, -10) == 20, "Should correctly sum mixed integers"


def test_my_sum_floats():
    assert my_sum(1, 2.5, 3, -0.5) == 6.0, "Should correctly sum floats"


def test_my_sum_single_argument():
    assert my_sum(
        3) == 3, "Should return the number itself when onlyone argument is given"


def test_my_sum_zero():
    assert my_sum(
        0, 0, 0, 0) == 0, "Should return zero when all arguments are zero"


def test_my_sum_large_number():
    assert my_sum(100000, 200000,
                  3000000) == 3300000, "Should handle large numberes correctly"


def test_my_sum_invalid_input():
    with pytest.raises(ValueError) as execinfo:
        my_sum(1, 2, 3, "Hello")
    assert str(execinfo.value) == "Only int or float are acceptable"


def test_my_sum_invalid_input_array():
    with pytest.raises(ValueError) as execinfo:
        my_sum(1, 2, 3, [1, 2, 3])
    assert str(execinfo.value) == "Only int or float are acceptable"
