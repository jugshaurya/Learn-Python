class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class QueueUsingLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self,data):
        self.count += 1        
        if self.head == None:
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        
    def dequeue(self):
        if self.head == None:
            return 0
        
        if self.head.next==None:
            element = self.head.data
            self.head = self.tail = None
            return element
        
        self.count -= 1
        element = self.head.data
        self.head = self.head.next
        
        return element

    def top(self):
        if self.head == None:
            return 0
        return self.head.data

    def empty(self):
        return self.head == None

    def size(self):
        return self.count
