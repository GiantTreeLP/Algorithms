import colorama


def hanoi(height: int, source_index: int, destination_index: int, external_index: int) -> None:
    """
    Recursive solution to solve the towers of hanoi problem.

    Computational complexity:

        A_n = A_n-1 + A_n-1 + 1

        A_n = 2 * A_n-1 + 1

        A_n = 2 * (2 * A_n-2 + 1) + 1

        A_n = 2 * 2 * A_n-2 + 2

        A_n = O(2^n)

    :param height: the height of the tower to solve
    :param source_index: the index of the source sublist in `towers`
    :param destination_index: the index of the destination sublist in `towers`
    :param external_index: the index of the external/third sublist in `towers`
    """
    if height == 1:
        towers[destination_index].append(towers[source_index].pop())
        print_towers(towers)
    else:
        hanoi(height - 1, source_index, external_index, destination_index)
        hanoi(1, source_index, destination_index, external_index)
        hanoi(height - 1, external_index, destination_index, source_index)


def hanoi_iter(height: int, source_index: int, destination_index: int, external_index: int) -> None:
    """
    Stack-based, iterative approach to solve the towers of hanoi problem.

    :param height: height of the tower to solve
    :param source_index: the index of the source sublist in `towers`
    :param destination_index: the index of the destination sublist in `towers`
    :param external_index: the index of the external/third sublist in `towers`
    """
    stack = [source_index, destination_index, external_index, height]
    while True:
        while height > 1:
            stack.append(source_index)
            stack.append(destination_index)
            stack.append(external_index)
            stack.append(height)
            height -= 1
            external_index, destination_index = destination_index, external_index
        towers[destination_index].append(towers[source_index].pop())
        print_towers(towers)
        height = stack.pop()
        external_index = stack.pop()
        destination_index = stack.pop()
        source_index = stack.pop()
        if len(stack) == 0:
            break
        towers[destination_index].append(towers[source_index].pop())
        print_towers(towers)
        height -= 1
        source_index, external_index = external_index, source_index


def print_towers(towers: list) -> None:
    """
    Clears the screen, prints the first three elements of a list and
    ends the block with 50 #'s.

    :param towers:
    """
    print('\033[2J')  # Clear terminal
    print(towers[0])
    print(towers[1])
    print(towers[2])
    print("#" * 50)


if __name__ == '__main__':
    colorama.init()  # Enable ANSI escape sequences
    towers = [list(range(10, 0, -1)), [], []]
    hanoi(len(towers[0]), 0, 1, 2)
    print_towers(towers)
    input()
    towers = [list(range(10, 0, -1)), [], []]
    hanoi_iter(len(towers[0]), 0, 1, 2)
    print_towers(towers)
    input()
