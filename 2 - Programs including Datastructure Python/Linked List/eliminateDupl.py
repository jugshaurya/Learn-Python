'''
Eliminate duplicates from LL
Given a sorted linked list (elements are sorted in ascending order). Eliminate duplicates from the given LL, 
such that output LL contains only unique elements.
You don't need to print the elements, just remove duplicates and return the head of updated LL.

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def eliminate_duplicate(head):
    
    if head == None or head.next == None:
        return head
    
    if head.data == head.next.data:
        return eliminate_duplicate(head.next)
    else:
        head.next = eliminate_duplicate(head.next)  
        return head
    
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
# Read the link list elements including -1
import sys
sys.setrecursionlimit(11000)
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = eliminate_duplicate(l)
printll(l)
