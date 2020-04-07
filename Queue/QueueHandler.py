import asyncio

class QueueHandler :
    _queue = asyncio.Queue()
    _queueLoop = asyncio.get_event_loop()

    def __init__(self):
        self._queueLoop.run_until_complete(self.run())
        #self._queueLoop.close()
    
    def __del__(self):
        self._queueLoop.close()

    async def Produce(self,name):
        await self._queue.put(name)

    async def Consume(self):
        while True:
            try:
                    
                item = await self._queue.get()
                print(item)
                self._queue.task_done()
            except:
                pass


    async def run(self):
        consumer = asyncio.ensure_future(self.Consume())
        await self.Produce("Amrish1")
        await self.Produce("Amrish2")
        await self.Produce("Amrish3")
        await self.Produce("Amrish4")
        await self._queue.join()
        consumer.cancel()
        

if __name__ == "__main__":
    c = QueueHandler()
    c.__del__()
        
