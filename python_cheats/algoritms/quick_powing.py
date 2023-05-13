def get_pow(a: float, n: int) -> float:
    """Returns a^n (a pow n)

    Args:
        a (float): number what is powing;
        n (int): number-power.

    Returns:
        float: powered bumber
    """
    assert type(a) == float or type(a) == int, "'a' must be a number"
    assert type(n) == int and n >= 0, "'n' must be integer and not sub 0"

    if n == 0:
        return 1
    elif n % 2 == 1:
        return get_pow(a, n - 1) * a
    else:
        return get_pow(a**2, n // 2)


print(get_pow(-3, 1300))
