from heapq import heappop, heappush


def selection_sort(sequence):
    swaps = 0
    comparisons = 0
    print("Length: %d" % len(sequence))
    for i in range(len(sequence)):
        smallest_index = i
        for j in range(i + 1, len(sequence)):
            comparisons += 1
            if sequence[j] < sequence[smallest_index]:
                smallest_index = j
        if smallest_index != i:
            sequence[i], sequence[smallest_index] = sequence[smallest_index], sequence[i]
            swaps += 1
    print("%d swaps" % swaps)
    print("%d comparisons" % comparisons)
    return sequence


def insertion_sort(sequence):
    swaps = 0
    comparisons = 0
    print("Length: %d" % len(sequence))
    for i in range(1, len(sequence)):
        to_sort = sequence[i]
        pos = i
        while pos > 0 and sequence[pos - 1] > to_sort:
            sequence[pos] = sequence[pos - 1]
            swaps += 1
            comparisons += 1
            pos -= 1
        sequence[pos] = to_sort
        swaps += 1
    print("%d swaps" % swaps)
    print("%d comparisons" % comparisons)
    return sequence


def merge_sort(x):
    if len(x) < 2:
        return x
    result = []
    mid = len(x) // 2
    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])
    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z.pop(0))
        else:
            result.append(y.pop(0))

    result.extend(y + z)
    return result


def quick_sort(x):
    if len(x) < 2:
        return x
    else:
        pivot = x[0]
        less = [i for i in x[1:] if i <= pivot]
        greater = [i for i in x[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def heap_sort(sequence):
    heap = []
    for v in sequence:
        heappush(heap, v)
    result = []
    while heap:
        result.append(heappop(heap))
    return result


if __name__ == '__main__':
    print(selection_sort([2, 4, 6, 4, 2, 7, 3, 1, 8, 6, 8, 4]))
    print(insertion_sort([2, 4, 6, 4, 2, 7, 3, 1, 8, 6, 8, 4]))
    print(merge_sort([2, 4, 6, 4, 2, 7, 3, 1, 8, 6, 8, 4]))
    print(quick_sort([2, 4, 6, 4, 2, 7, 3, 1, 8, 6, 8, 4]))
    print(heap_sort([2, 4, 6, 4, 2, 7, 3, 1, 8, 6, 8, 4]))
