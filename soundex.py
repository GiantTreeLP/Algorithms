from typing import Dict

classification: Dict[str, str] = {
    'B': '1',
    'C': '2',
    'D': '3',
    'F': '1',
    'G': '2',
    'J': '2',
    'K': '2',
    'L': '4',
    'M': '5',
    'N': '5',
    'P': '1',
    'Q': '2',
    'R': '6',
    'S': '2',
    'T': '3',
    'V': '1',
    'X': '2',
    'Z': '2'
}


def soundex(s: str) -> str:
    s = s.upper()
    result = s[0]
    for i in range(1, len(s)):
        if s[i] != s[i - 1] and s[i] in classification:
            result += classification[s[i]]
    result = result.ljust(4, '0')[0:4]
    return result


if __name__ == '__main__':
    print(soundex("Meier"))
    print(soundex("Meyer"))
    for name in open("resources/nachnamen.txt"):
        name = name.strip()
        if soundex("Meier") == soundex(name):
            print(name, soundex(name))
