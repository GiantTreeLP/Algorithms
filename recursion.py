def fact(n: int) -> int:
    """
    Recursive faculty calculation.
    Fails at small numbers, due to the low recursion depth

    Computational complexity:

        A_n = A_n-1 + 1

        A_n = O(A_n)

        A_n = O(n)

    :param n: a number, small enough to not crash Python
    :return: the faculty of n
    """
    if n < 2:
        return 1
    return n * fact(n - 1)


def iter_fact(n: int) -> int:
    """
    Iterative calculation of the faculty of n

    Computational complexity:

        A_n = A_n-1 + 1

        A_n = n * 1

        A_n = O(n)

    :param n: parameter for `n!`
    :return: the faculty (`n!`) of n
    """
    f = n
    n -= 1
    while n:
        f *= n
        n -= 1
    return f


def fib(n: int) -> int:
    """
    Recursive approach to calculate the n-th fibonacci number.
    Very slow at relatively small numbers.

    Computational complexity:

        A_n = A_n-1 + A_n-2

        A_n = O(2 * A_n-1)

        A_n = O(2^n)

    :param n: the index for the fibonacci sequence
    :return: the n-th fibonacci number
    """
    if n < 2:
        return 1
    return fib(n - 2) + fib(n - 1)


def iter_fib(n: int) -> int:
    """
    Iterative approach to calculate the n-th fibonacci number.

    :param n: the index of the fibonacci number to calculate
    :return: the n-th fibonacci number
    """
    a: int = 1
    b: int = 1
    for i in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    print(fact(99))
    print(iter_fact(99))
    print(fib(30))
    print(iter_fib(30))
    print(iter_fib(1000000))
