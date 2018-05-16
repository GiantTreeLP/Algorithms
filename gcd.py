def gcd(a: int, b: int) -> int:
    """
    Calculates the greatest common divider of a and b.

    :param a: an integer
    :param b: another integer
    :return: the greatest common divider of a and b
    """
    while a > 0:
        if a < b:
            a, b = b, a
        a %= b
    return b


if __name__ == '__main__':
    print(gcd(
        int(input("Erste Zahl: ")),
        int(input("Zweite Zahl: "))
    ))
