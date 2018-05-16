class Node:
    """
    Data structure that holds a value and a pointer to the next instance of this class.
    That pointer is `None` in the event that there is no next instance.
    """

    def __init__(self, value: object):
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return repr(self.value)


class List:
    """
    Simple singly-linked list

    Exposes iterator, queue and stack functionality
    """

    def __init__(self):
        self.head = Node(None)
        self.length = 0
        self.tail = self.head

    def __len__(self) -> int:
        """
        Returns the length of this list without iterating over it.

        :return: the length of this list
        """
        return self.length

    def __iter__(self) -> object:
        """
        An iterator over all the nodes that make up this list.
        Yields the nodes' values.

        :return: an iterator yielding node values
        """
        node = self.head
        while node.next is not None:
            node = node.next
            yield node.value

    def __str__(self) -> str:
        """
        Joins the string representations of this list's nodes.

        :return: the string representation of this list
        """
        return "[" + ", ".join(repr(e) for e in self) + "]"

    def append(self, value: object) -> None:
        """
        Adds a new node containing the given value to this list.

        :param value: value to add to this list
        """
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.length += 1

    def insert(self, index: int, value: object) -> None:
        """
        Inserts a node containing the value at the given index shifting all nodes after that
        one index further.
        If the index is greater than the length, appends instead.

        :param index: index to insert at
        :param value: value to insert
        """
        if index > len(self):
            self.append(value)
            return
        node = self.head
        for i in range(index):
            #  if node.next is not None:
            #  No need to check because the bounds are already checked.
            node = node.next
        temp = node.next
        new_node = Node(value)
        new_node.next = temp
        node.next = new_node
        self.length += 1

    def remove(self, index: int) -> object:
        """
        Removes the node at the given index.
        If the list has less nodes than the index, removes the last one.

        :param index: index to remove the node at
        :return: the removed node's value
        """
        before = self.head
        node = self.head.next
        for i in range(index):
            if node.next is not None:
                before = node
                node = node.next
        before.next = node.next
        self.length -= 1
        return node.value

    def push(self, value: object) -> None:
        """
        Pushes a node containing the given value to the head of the list.

        :param value: value to add
        """
        temp = self.head.next
        self.head.next = Node(value)
        self.head.next.next = temp
        self.length += 1

    def pop(self) -> object:
        """
        Removes and returns the value of the node at the head.

        :return: the value of the node at the head
        """
        node = self.head.next
        self.head.next = self.head.next.next
        self.length -= 1
        return node.value

    def __getitem__(self, index: int) -> object:
        """
        Convenience method to get the value of the node at a given index using the Python array accessor.

        :param index: index to get the value at
        :return: the value of the node at index
        """
        node = self.head.next
        for i in range(index):
            node = node.next
        return node.value

    def get_node(self, index: int) -> Node:
        """
        Traverses the list and returns the node at the given index.

        :param index: 0-based index
        :return: Node at index
        """
        node = self.head.next
        for i in range(index):
            node = node.next
        return node

    def __setitem__(self, index: int, value: object) -> None:
        """
        Convenience method that allows the use of the Python array setter.
        Appends a new node if the index is out of bounds.

        :param index: index to set the value at
        :param value: the new value of the node at index
        """
        if index >= len(self):
            self.append(value)
        else:
            self.get_node(index).value = value


if __name__ == '__main__':
    pass
