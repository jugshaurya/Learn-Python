class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge(head1,head2):
    
    newhead = None
    if head1.data <= head2.data:
        newhead = head1
        head1 = head1.next
    else:
        newhead = head2
        head2 = head2.next
        
    temp = newhead
    while head1 is not None and head2 is not None :
        if head1.data <= head2.data:
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next
        temp = temp.next
        
    if head1 is not None:
        temp.next = head1
        
        
    if head2 is not None:
        temp.next = head2

    return newhead
    
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

arr1=list(int(i) for i in input().split())
arr2=list(int(i) for i in input().split())
l1 = ll(arr1[:-1])
l2 = ll(arr2[:-1])
l = merge(l1, l2)
printll(l)