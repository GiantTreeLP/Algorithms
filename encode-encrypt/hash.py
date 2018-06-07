def hash_string(string: str, modulo: int = 97, base: int = 30) -> int:
    """
    Hashes the given string by multiplying the integer corresponding to the current character in the string
    with the n-th power of the `base`.
    Calculates the hash in reverse order of the string.

    :param string: The string to hash, *HAS* to be all UPPERCASE
    :param modulo: the modulo to constrain the hash by
    :param base: the base to use for the calculation
    :return: the hashcode in the range of 0 to `modulo` (exclusive)
    """
    b = 1
    n = 0

    for c in string[::-1]:
        n += ((ord(c) - ord('A') + 1) * b)
        n %= modulo
        b *= base
        b %= modulo
    return n


if __name__ == '__main__':
    print(hash_string("ALGORITHMUS"))
