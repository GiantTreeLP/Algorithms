import json
import os
from heapq import heapify, heappop, heappush
from pathlib import Path
from typing import Dict, List, Tuple, Iterable


def frequency(input_bytes: Iterable) -> Dict[chr, int]:
    result = {}
    for c in input_bytes:
        c = chr(c)
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result


def init_heap(frequencies: Dict[chr, int]) -> List[Tuple[int, List[Tuple[chr, Tuple[int, int]]]]]:
    heap = [(f, [(s, (0, 0))]) for s, f in frequencies.items()]
    heapify(heap)
    return heap


def encode(input_bytes: Iterable[int], table: Dict[chr, Tuple[int, int]]) -> str:
    result: str = ""
    for s in input_bytes:
        b, v = table[chr(s)]
        result += format_binary(b, v)
    return result


def format_binary(b: int, v: int) -> str:
    return bin(v)[2:].rjust(b, '0')


def encoding_table(input_bytes: Iterable[int]) -> Dict[int, Tuple[int, int]]:
    frequencies = frequency(input_bytes)
    heap = init_heap(frequencies)
    while len(heap) > 1:
        a = heappop(heap)
        b = heappop(heap)
        merged = (a[0] + b[0],
                  [(s, (n + 1, v)) for (s, (n, v)) in a[1]]
                  + [(s, (n + 1, (1 << n) + v)) for (s, (n, v)) in b[1]])
        heappush(heap, merged)
    return dict(heappop(heap)[1])


def compress(encoded: str) -> Tuple[bytes, int]:
    padding = (8 - (len(encoded) % 8)) % 8
    encoded += '0' * padding
    array = bytes([int(encoded[i:i + 8], 2) for i in range(0, len(encoded), 8)])
    return array, padding


def decompress(compressed: bytes) -> str:
    return ''.join([format_binary(8, b) for b in compressed])


def write_to_file(file_name: str, compressed: bytes, table: Dict[int, Tuple[int, int]], padding: int) -> None:
    with open(file_name, mode="wb") as f:
        obj = {'p': padding,
               't': table}
        f.write(json.dumps(obj, ensure_ascii=False, separators=(',', ':')).encode('UTF-8'))
        f.write(bytes([0]))
        f.write(compressed)
        f.close()


def compress_to_file(file_name: str, input_bytes: Iterable[int]) -> None:
    table = encoding_table(input_bytes)
    compressed, padding = compress(encode(input_bytes, table))
    write_to_file(file_name, compressed, table, padding)


def read_from_file(file_name: str) -> bytes:
    binary = Path(file_name).read_bytes()
    null_index = binary.find(0)
    obj = json.loads(binary[0:null_index], encoding='UTF-8')
    compressed = binary[null_index + 1:]
    decompressed = decompress(compressed)[0:len(compressed) * 8 - obj['p']]
    return decode(decompressed, obj['t'])


def decode(encoded: str, table: Dict[chr, Tuple[int, int]]) -> bytes:
    decoding_table = dict()
    for s, (b, v) in table.items():
        decoding_table[format_binary(b, v)] = (s, b)
    i: int = 0
    code_len: int = 1
    result = b""
    while i < len(encoded):
        code = encoded[i:i + code_len]
        if code in decoding_table:
            decoded = decoding_table[code]
            result += bytes([ord(decoded[0])])
            # encoded = encoded[0:i] + decoded[0] + encoded[i + code_len:]
            i += code_len
            code_len = 1
        else:
            code_len += 1
    return result


if __name__ == '__main__':
    text = Path('../resources/loremipsum.txt').read_bytes()
    compress_to_file("compressed.huff", text)

    iterable = read_from_file("compressed.huff")
    print("Size original:", len(text))
    print("Size compressed:", os.stat("compressed.huff").st_size)
    print("Net savings: {:%}".format(1 - os.stat("compressed.huff").st_size / len(text)))
