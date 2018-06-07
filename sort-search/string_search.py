from typing import List


def brute_force_search(needle: str, haystack: str) -> int:
    m = len(needle)
    haystack += needle
    i = j = 0
    while j < m:
        while haystack[i] != needle[j]:
            i += 1 - j
            j = 0
        i += 1
        j += 1
    return i - m


def kmp_search(needle: str, haystack: str) -> int:
    def initnext(s: str) -> List[int]:
        n = [0] * (len(s) + 1)
        n[0] = -1
        i = 0
        j = -1
        while i < len(s):
            while j >= 0 and s[i] != s[j]:
                j = n[j]
            i += 1
            j += 1
            n[i] = j
        return n

    m = len(needle)
    n = initnext(needle)
    haystack += needle

    i = j = 0
    while j < m:
        while j >= 0 and haystack[i] != needle[j]:
            j = n[j]
        i += 1
        j += 1
    return i - m


def boyer_moore_search(needle: str, haystack: str) -> int:
    def initskip(s: str) -> List[int]:
        skip = [0] * 256
        m = len(s)
        for j in range(256):
            skip[j] = m
        for j in range(len(s)):
            skip[ord(s[j])] = m - j - 1
        return skip

    m = len(needle)
    skip = initskip(needle)
    i = j = m - 1
    while j > 0:
        while haystack[i] != needle[j]:
            t = skip[ord(haystack[i])]
            i += max(m - j, t)
            j = m - 1
        i -= 1
        j -= 1
    return i


def rabin_karp_search(needle: str, haystack: str) -> int:
    b = 256
    q = 8388593
    m = len(needle)
    B = b ** (m - 1)
    hp = ha = 0
    haystack += needle
    for i in range(m):
        hp = (hp * b + ord(needle[i])) % q
        ha = (ha * b + ord(haystack[i])) % q
    i = 0
    while hp != ha:
        ha = (ha - B * ord(haystack[i])) % q
        ha = (ha * b + ord(haystack[i + m])) % q
        i += 1
    return i


if __name__ == '__main__':
    print(brute_force_search("fox", "The lazy brown fox jumps over the lazy dog"))
    print(kmp_search("fox", "The lazy brown fox jumps over the lazy dog"))
    print(boyer_moore_search("fox", "The lazy brown fox jumps over the lazy dog"))
    print(rabin_karp_search("fox", "The lazy brown fox jumps over the lazy dog"))
    print("The lazy brown fox jumps over the lazy dog".find("fox"))
