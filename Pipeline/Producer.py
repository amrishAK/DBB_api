from queue import Queue

class Producer:

    count = 0
    def __init__(self):
        self._queue = Queue()

    def Produce(self):
        self.count += 1
        self._queue.put("Item" + str(self.count))