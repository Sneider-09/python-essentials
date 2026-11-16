class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.__queue_list = []
    
    def put(self, val):
        self.__queue_list.insert(0,val)
    
    def get(self):
        if len(self.__queue_list) > 0:
            val = self.__queue_list[-1]
            del self.__queue_list[-1]
            return val
        else:
            raise QueueError
        
    

que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")