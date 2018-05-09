class Queue:

    def __init__(self):
        self.queue = []

    def put(self, value):
        self.queue.append(value)

    def get(self):
        return self.queue.pop(0)


if __name__ == '__main__':
    queue = Queue()
    queue.put("A")
    queue.put("B")
    print(queue.get())
