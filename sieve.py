from math import sqrt


def sieve(n):
    b = [True] * n
    b[1] = False
    for i in range(1, round(sqrt(n))):
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
