from typing import List

import math


def sieve(n: int) -> List[int]:
    """
    Determines the prime numbers between 0 and n using the sieve of eratosthenes with a size of n.

    :param n: size of the sieve
    :return: the prime numbers between 0 and n
    """
    b = [True] * n
    b[1] = False
    for i in range(1, round(math.sqrt(n))):
        if b[i]:
            for j in range(i * i, n, i):
                b[j] = False
    nums = []
    k = 0
    for i in range(1, n):
        k += 1
        if b[i]:
            nums.append(i)
    return nums


if __name__ == '__main__':
    s = sieve(1000)
    print("Found %s primes" % len(s))
    print(s)
