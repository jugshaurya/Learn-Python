class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseRecursive(head):
    
    if head==None or head.next == None:
        return head
    
    smallhead = reverseRecursive(head.next)
    head.next.next = head
    head.next = None
    return smallhead
    
def reverse(head):
    if head == None or head.next == None:
        return head
    
    prev = None
    curr = head
    upcoming = None
    while curr is not None :
        upcoming = curr.next
        curr.next = prev
        prev = curr
        curr = upcoming
    
    return prev

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

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
arr=list(int(i) for i in input().split())
l = ll(arr[:-1])
l = reverseRecursive(l)
printll(l)
l = reverse(l)
printll(l)
