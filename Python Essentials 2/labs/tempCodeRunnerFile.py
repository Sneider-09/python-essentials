class Queue:
    def __init__(self):
        self.queue_list = []
    
    def put(self, val):
        self.queue_list.insert(0,val)
    
    def get(self):
        if len(self.queue_list) > 0:
            val = self.queue_list[-1]
            del self.queue_list[-1]
            return val
        else:
            raise QueueError


class SuperQueue(Queue):
    def validate(self):
        if len(self.queue_list) > 0:
            return True
        else:
            return False