from queue import Queue
import threading
from Pipeline.Producer import Producer
import json
import socket
from Helper.JsonHandler import JsonHandler



class Consumer:

    def __init__(self, producer : Producer):
        self._JsonHandler = JsonHandler()
        self.config = self._JsonHandler.LoadJson('Config.json')
        self._queue = producer._queue
        self.socketClosed = False
        self._thread = threading.Thread(target=self.Consume)
        self._thread.daemon = True
        self._thread.start()


    def Consume(self):
        print("Started consuming")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.config['CordinatorHost'], self.config['CordinatorSocketPort']))
        msg = {"type" : "DataSource", "source" : "participant"}
        client.send(bytes(json.dumps(msg), "utf8"))
        while True:
            try:
                item = self._queue.get()
                while True:
                    try:
                        if self.socketClosed:
                            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            client.connect(('localhost', 7000))
                        client.send(bytes(json.dumps(item), "utf8"))
                        break
                    except:
                        self.socketClosed = True
                        client.close()
                        continue
                self._queue.task_done()
            except:
                continue

            