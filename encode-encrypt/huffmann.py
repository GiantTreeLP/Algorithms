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
    heap.append((1, [(0, (0, 0))]))
    heapify(heap)
    return heap


def encode(input_bytes):
    frequencies = frequency(input_bytes)
    heap = initheap(frequencies)
    while len(heap) > 1:
        a = heappop(heap)
        b = heappop(heap)
        merged = (a[0] + b[0],
                  [(s, (n + 1, v)) for (s, (n, v)) in a[1]]
                  + [(s, (n + 1, (1 << n) + v)) for (s, (n, v)) in b[1]])
        heappush(heap, merged)
    table = dict(heappop(heap)[1])
    # print(table)
    # print("bits    code          value    symbol")
    # for s, (b, v) in table.items():
    #     print("{b:4d}\t{c:14s}\t{v:5d}\t{s!r}".format(
    #         b=b, v=v, s=s, c=bin(v)[2:].rjust(b, '0')
    #     ))
    for s in input_bytes:
        b, v = table[s]
        yield "{b:0b}".format(b=v)


def test_encode() -> None:
    input_bytes = Path("../resources/loremipsum.txt").read_text()
    print("".join(encode(input_bytes)))


if __name__ == '__main__':
    test_encode()
