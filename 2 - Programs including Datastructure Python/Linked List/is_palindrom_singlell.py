class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def midpoint(head):
    if head == None or head.next == None:
        return head
    
    slow, fast = head, head.next
    while fast is not None and fast.next is not None :
        slow = slow.next
        fast = fast.next.next
    
    return slow

def midpoint(head):
    if head == None or head.next == None:
        return head
    
    slow, fast = head, head.next
    while fast is not None and fast.next is not None :
        slow = slow.next
        fast = fast.next.next
    
    return slow

def reverse(head):
    
    if head==None or head.next == None :
        return head
    
    prev = None
    curr = head
    upcoming = None
    while curr is not None :
        upcoming = curr.next
        curr.next = prev
        prev = curr
        curr = upcoming
    
    newhead = prev
    return newhead

def check_palindrome(head) :
    
    mid_node = midpoint(head)
    next_to_mid_node = mid_node.next
    mid_node.next = None
    l1 = head
    l2 = next_to_mid_node
    l2 = reverse(l2)
    
    while l2 is not None:
        if  l1.data != l2.data:
            return False
        l1 = l1.next
        l2 = l2.next
    
    return True
    
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
ans = check_palindrome(l)
if ans:
    print("true")
else:
    print("false")

