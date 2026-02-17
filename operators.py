def add(a, b):
    """
    Adds two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first.

    Args:
        a (float): The minuend.
        b (float): The subtrahend.

    Returns:
        float: The difference between a and b.
    """
    return b - a  # there is a bug here

def multiply(a, b):
    """
    Multiplies two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of a and b.
    """
    return a ** b  # there is a bug here

def divide(a, b):
    """
    Divides the first number by the second.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The quotient of a and b.

    Raises:
        ValueError: If b is zero.
    """
    return a // b  # there is a bug here
