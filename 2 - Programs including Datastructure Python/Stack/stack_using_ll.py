
class StackLL :

    class Node : 
        def __init__(self,data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.count = 0

    def push(self ,data):
        # pushing at head is O(1) so pushing at head and then changing head
        newNode = StackLL.Node(data)
        if self.head == None :
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.count += 1

    def pop(self):

        # poping from head is O(1) so poping at head and then changing head
        if self.head == None:
            return None
        else :
            data = self.head.data
            self.head = self.head.next
            self.count -= 1
            return data

    def top(self):
        if self.head == None:
            return None
        else :
            return self.head.data

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0
