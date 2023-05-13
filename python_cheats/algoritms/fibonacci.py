
import sys
sys.setrecursionlimit(10000)
_count = 0  # count of recursions
cache = {0: 1, 1: 1}


def fib(n: int) -> int:
    """Returns Fibonacci number. Works with cache.

    Args:
        n (int): number for find Fibonacci of

    Returns:
        int: Fibonacci number of input bumber
    """
    global _count
    global cache
    _count += 1
    if n not in cache:
        cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]


print(f"Fibonacci number - {fib(1000)}")
print(f"Count of recursions - : {_count}.")
