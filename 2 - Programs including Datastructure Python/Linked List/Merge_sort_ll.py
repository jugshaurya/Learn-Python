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

def midpoint(head):
    if head == None or head.next == None:
        return head
    
    slow, fast = head, head.next
    while fast is not None and fast.next is not None :
        slow = slow.next
        fast = fast.next.next
    
    return slow
    
def mergeSort(head):
    
    if head==None or head.next == None:
        return head
    
    mid_node = midpoint(head)
    next_node_of_mid = mid_node.next
    mid_node.next = None
    
    ll1_head = head
    ll2_head = next_node_of_mid
    new_ll1 = mergeSort(ll1_head)
    new_ll2 = mergeSort(ll2_head)
    return merge(new_ll1 ,new_ll2)
    
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

arr=list(int(i) for i in input().split())
l = ll(arr[:-1])
l = mergeSort(l)
printll(l)
