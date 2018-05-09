class Queue(list):
    def put(self, value):
        self.append(value)

    def get(self):
        return self.pop(0)


if __name__ == '__main__':
    queue = Queue()
    queue.put("A")
    queue.put("B")
    print(queue.get())
    print(queue)
