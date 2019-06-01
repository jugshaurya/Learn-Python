class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def midpoint_linkedlist(head):
    if head == None or head.next == None:
        return head
    
    # in case of odd length list like 5 , we return 2 (5 // 2) 
    # in case of even length list like 6 , we return 3(6//2) , our wish
    slow, fast = head, head
    while fast is not None and fast.next is not None :
        slow = slow.next
        fast = fast.next.next
    
    return slow


def midpoint_linkedlist2(head):
    if head == None or head.next == None:
        return head
    
    # in case of odd length list like 5 , we return 2 (5 // 2) 
    # in case of even length list like 6 , we return 2(6//2 -1), our wish
    slow, fast = head, head.next # fast being ahead by one initially
    while fast is not None and fast.next is not None :
        slow = slow.next
        fast = fast.next.next
    
    return slow
    
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

arr=list(int(i) for i in input().split())
l = ll(arr[:-1])

node = midpoint_linkedlist(l)
if node:
    print(node.data)


node = midpoint_linkedlist2(l)
if node:
    print(node.data)
