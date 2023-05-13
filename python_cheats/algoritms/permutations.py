# best choise to use intertools
# import intertools

def gen_permutations(n: int, m: int = -1, prefix=None) -> None:
    """Generates all pemutations of 'n' numbers in 'm' positions with prefix 'prefix'

    Args:
        n (int): quantity of numbers
        m (int): quantity of positions
        prefix (list, optional): for saving temporary results. Defaults to None.

    Returns:
        none: just prints in console
    """
    assert m >= -1 and m <= n, "'m' must be greater tnan 0 and LE than 'n'"
    assert n > 0, "'n' must be greater tnan 0"
    if m == -1:
        m = n
    prefix = prefix or []
    if m == 0:
        print(*prefix)
        return
    #
    for number in range(1, n + 1):
        if prefix.count(number):  # if number exists in prefix
            continue
        prefix.append(number)
        gen_permutations(n, m-1, prefix)
        prefix.pop()


gen_permutations(3, 3)
