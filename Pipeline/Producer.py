from queue import Queue

class Producer:

    def __init__(self):
        self._queue = Queue()

    def Produce(self,payload):
        print("Produced")
        self._queue.put({"payload" : payload, "type" : "data", "source" : "primaryReplica"})