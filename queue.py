class Queue(list):
    """
    Lazy queue implementation
    """

    def put(self, value):
        """
        Puts a value at the end of the queue.

        :param value: the value to add to the queue
        """
        self.append(value)

    def get(self):
        """
        Gets the next value of the queue.

        :return: the next element in the queue
        """
        return self.pop(0)


if __name__ == '__main__':
    queue = Queue()
    queue.put("A")
    queue.put("B")
    print(queue.get())
    print(queue)
