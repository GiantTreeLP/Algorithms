class List:
    """
    Simple singly-linked list

    Exposes iterator, queue and stack functionality
    """

    def __init__(self):
        self.head = Node(None)
        self.length = 0
        self.tail = self.head

    def __len__(self):
        return self.length

    def __iter__(self):
        node = self.head
        while node.next is not None:
            node = node.next
            yield node

    def __str__(self):
        return "[" + ", ".join(repr(e) for e in self) + "]"

    def append(self, other):
        self.tail.next = Node(other)
        self.tail = self.tail.next
        self.length += 1

    def insert(self, index, other):
        if index > len(self):
            self.append(other)
            return
        node = self.head
        for i in range(index):
            if node.next is not None:
                node = node.next
        temp = node.next
        new_node = Node(other)
        new_node.next = temp
        node.next = new_node
        self.length += 1

    def remove(self, index):
        before = self.head
        node = self.head.next
        for i in range(index):
            if node.next is not None:
                before = node
                node = node.next
        before.next = node.next
        self.length -= 1
        return node.value

    def push(self, value):
        temp = self.head.next
        self.head.next = Node(value)
        self.head.next.next = temp
        self.length += 1

    def pop(self):
        node = self.head.next
        self.head.next = self.head.next.next
        self.length -= 1
        return node.value

    def __getitem__(self, index):
        node = self.head.next
        for i in range(index):
            node = node.next
        return node.value

    def get_node(self, index):
        """
        Traverses the list and returns the node at the given index.

        :param index: 0-based index
        :return: Node at index
        """
        node = self.head.next
        for i in range(index):
            node = node.next
        return node

    def __setitem__(self, index, value):
        if index >= len(self):
            self.append(value)
        else:
            self.get_node(index).value = value


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return repr(self.value)


if __name__ == '__main__':
    liste = List()

    liste.push("Vorne")
    print(liste)
    print(liste.pop())
    print(liste)
