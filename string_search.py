def brute_force_search(needle, haystack):
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


def kmp_search(needle, haystack):
    def initnext(s):
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


if __name__ == '__main__':
    print(brute_force_search("fox", "The lazy brown fox jumps over the lazy dog"))
    print(kmp_search("fox", "The lazy brown fox jumps over the lazy dog"))
    print("The lazy brown fox jumps over the lazy dog".find("fox"))
