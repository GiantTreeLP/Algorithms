def rot13(s: str) -> str:
    r: str = ""
    for c in s.upper():
        if c.isspace():
            r += " "
        elif c.isalpha():
            r += chr(((ord(c) - ord('A') + 13) % 26) + ord('A'))
    return r


if __name__ == '__main__':
    print(rot13("rot dreizehn"))
    print(rot13("EBG QERVMRUA"))
