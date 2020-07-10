
class QueueUsingArr:
    def __init__(self):
        self.arr = []
        self.count = 0
        self.front = -1 # always access the start + 1 element while popping

    def enqueue(self,data):
        self.arr.append(data)
        self.count += 1

    def dequeue(self):
        if self.empty():
            return 0 # if empty returning  0 to show queue is empty
        self.count -= 1

        element = self.arr[self.front + 1]
        self.front += 1
        return element

    def top(self):
        if self.empty():
            return 0
        
        return self.arr[self.front + 1]

    def empty(self):
        return self.count == 0

    def size(self):
        return self.count   

