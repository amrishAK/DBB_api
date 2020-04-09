from queue import Queue
import threading
from Pipeline.Producer import Producer


class Consumer:

    def __init__(self, producer : Producer):
        self._queue = producer._queue
        self._thread = threading.Thread(target=self.Consume)
        self._thread.daemon = True
        self._thread.start()


    def Consume(self):
        while True:
            try:
                item = self._queue.get()
                print(item)
                self._queue.task_done()
            except:
                continue

            