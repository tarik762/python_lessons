N = 1


def get_factorial(n: int) -> int:
    """Calculate factorial of input namber 'n'

    Args:
        n (int): input number

    Returns:
        int: factorial of number 'n'
    """
    assert n >= 0, "Input number 'n' is negative, please fix it."
    if n == 1 or n == 0:
        return n
    return get_factorial(n - 1) * n


print(get_factorial(9))
