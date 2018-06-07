from array import array


class Stack(array):
    """
    Stack based on an array
    """

    def push(self, value: object):
        """
        Push value to the top of the stack.

        :param value: value to push to the stack
        """
        self.append(value)


if __name__ == '__main__':
    stack = Stack("u")
    stack.push("A")
    stack.push("B")
    stack.push("C")
    stack.push("D")
    print(stack.pop())
    print(stack)

    stack = Stack('I')
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack)
