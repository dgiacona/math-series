from series import fibonacci
from series import lucas
from series import sum_series

def test_fibonacci():
    actual = fibonacci(8)
    expected = 34
    assert actual == expected

def test_lucas():
    actual = lucas(8)
    expected = 47
    assert actual == expected

def test_sum_series():
    actual = sum_series(2, 3, 4)
    expected = 7
    assert actual == expected
    

