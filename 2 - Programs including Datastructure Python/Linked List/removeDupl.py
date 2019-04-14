'''
Eliminate duplicates from LL
Given a sorted linked list (elements are sorted in ascending order). Eliminate duplicates from the given LL, such that output LL contains only unique elements.
You don't need to print the elements, just remove duplicates and return the head of updated LL.
Input format : Linked list elements (separated by space and terminated by -1)

Sample Input 1 :
1 2 3 3 3 4 4 5 5 5 7 -1
Sample Output 1 :
1 2 3 4 5 7
Download Test Cases
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def eliminate_duplicate_recursive(head):
    
    if head == None or head.next == None:
        return head
    
    if head.data == head.next.data:
        return eliminate_duplicate_recursive(head.next)
    else:
        head.next = eliminate_duplicate_recursive(head.next)  
        return head

def eliminate_duplicate(head):
    if head==None or head.next == None:
        return head
    
    temp = head
    while temp.next != None:
        if temp.data == temp.next.data :
            temp.next = temp.next.next
        else:
            temp = temp.next
            
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

# Read the link list elements including -1
arr=list(int(i) for i in input().split())
l = ll(arr[:-1])
l = eliminate_duplicate(l)
printll(l)
