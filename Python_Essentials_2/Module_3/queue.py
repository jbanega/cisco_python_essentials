class QueueError(IndexError):
    def __init__(self):
        IndexError.__init__(self)


class Queue:
    def __init__(self):
        self._queue_list = []
    
    def put(self, elem):
        self._queue_list.insert(0, elem)

    def get(self):
        try:
            val = self._queue_list[-1]
            del self._queue_list[-1]
            return val
        except:
            raise QueueError


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    
    def isempty(self):
        if len(self._queue_list) == 0:
            return True
        else:
            return False


# Exercise 1
que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")


# Exercise 2
print()
que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")