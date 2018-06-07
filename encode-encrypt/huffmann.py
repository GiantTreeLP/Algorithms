from heapq import heapify, heappop, heappush
from pathlib import Path
from typing import Dict, List


def frequency(input_bytes) -> Dict[object, int]:
    result = {}
    for c in input_bytes:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result


def initheap(frequencies) -> List[object]:
    heap = [(f, [(s, (0, 0))]) for s, f in frequencies.items()]
    heapify(heap)
    return heap


def encode(input_bytes, table):
    result: str = ""
    for s in input_bytes:
        b, v = table[s]
        result += format_binary(b, v)
    return result


def format_binary(b, v):
    return bin(v)[2:].rjust(b, '0')


def encoding_table(input_bytes):
    frequencies = frequency(input_bytes)
    heap = initheap(frequencies)
    while len(heap) > 1:
        a = heappop(heap)
        b = heappop(heap)
        merged = (a[0] + b[0],
                  [(s, (n + 1, v)) for (s, (n, v)) in a[1]]
                  + [(s, (n + 1, (1 << n) + v)) for (s, (n, v)) in b[1]])
        heappush(heap, merged)
    return dict(heappop(heap)[1])


def test_encode() -> None:
    input_bytes = Path("../resources/loremipsum.txt").read_text()
    table = encoding_table(input_bytes)
    encoded = encode(input_bytes, table)
    print(encoded)
    decoded = decode(encoded, table)
    print(decoded)


def decode(encoded, table):
    decoding_table = dict()
    for s, (b, v) in table.items():
        decoding_table[format_binary(b, v)] = (s, b)
    i: int = 0
    code_len: int = 1
    while i < len(encoded):
        code = encoded[i:i + code_len]
        if code in decoding_table:
            decoded = decoding_table[code]
            encoded = encoded[0:i] + decoded[0] + encoded[i + code_len:]
            i += 1
            code_len = 1
        else:
            code_len += 1
    return encoded


if __name__ == '__main__':
    test_encode()
