
def get_gcd(a: int, b: int) -> int:
    """Returns greatest common divider of two numbers

    Args:
        a (int): 1st number
        b (int): 2nd number

    Returns:
        int: greatest common divider of two numbers
    """
    assert type(a) == int, "'a' must be integer"
    assert type(b) == int, "'b' must be integer"

    return a if b == 0 else get_gcd(b, a % b)


print(get_gcd(16, 440))
