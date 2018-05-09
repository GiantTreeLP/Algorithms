from array import array


class Stack:
    """
    Stack based on an array
    """

    def __init__(self, type_code='u'):
        """
        Creates an array of type `type_code`.
        Refer to https://docs.python.org/2/library/array.html for a list of type codes.

        :param type_code: the type of the values store in the array. Defaults to unicode characters.
        """
        self.backing_array = array(type_code)

    def __repr__(self):
        return repr(self.backing_array)

    def push(self, value):
        self.backing_array.append(value)

    def pop(self):
        value = self.backing_array[0]
        self.backing_array.remove(value)
        return value


if __name__ == '__main__':
    stack = Stack()
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
