from typing import Tuple, Dict

from pympler import asizeof


def ackermann(m: int, n: int) -> int:
    """
    Resursive approach to solve the ackermann function.

    :param m: first parameter
    :param n: second parameter
    :return: ackermann(m, n)
    """
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


def ackermann_iter(m: int, n: int) -> int:
    stack = [m]
    while stack:
        m = stack.pop()
        if m == 0:
            n += 1
        elif n == 0:
            n = 1
            m -= 1
            stack.append(m)
        else:
            stack.append(m - 1)
            stack.append(m)
            n -= 1
    return n


def ackermann_mem(m: int, n: int) -> int:
    if (m, n) in memory:
        return memory[(m, n)]
    if m == 0:
        memory[(m, n)] = n + 1
    elif n == 0:
        memory[(m, n)] = ackermann_mem(m - 1, 1)
    else:
        memory[(m, n)] = ackermann_mem(m - 1, ackermann_mem(m, n - 1))
    return memory[(m, n)]


if __name__ == '__main__':
    print(ackermann(3, 6))
    print(ackermann_iter(3, 6))
    memory: Dict[Tuple[int, int], int] = {}
    try:
        print(ackermann_mem(4, 1))
    except Exception as e:
        print(e)
    print(memory)
    print("%f kB" % round(asizeof.asizeof(memory) / 1024))
