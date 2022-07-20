from series import fibonacci
from series import lucas

def test_fibonacci():
    actual = fibonacci(8)
    expected = 34
    assert actual == expected

def test_lucas():
    actual = lucas(8)
    expected = 47
    assert actual == expected
    

