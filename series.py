# create a fibonacci function
def fibonacci (n):
    """
    Created the fibonacci function that takes in n and returns the correct
    fibonacci number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
    Similar to fibonacci function that takes in n and returns the correct
    Lucas number.
    """
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, a=1, b=1):
    """
    Description
    """





print(fibonacci(8))
print(lucas(8))

