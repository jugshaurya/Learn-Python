'''
Even after Odd LinkedList
Arrange elements in a given Linked List such that, all even numbers are placed after odd numbers. Respective order of elements should remain same.
You don't need to print the elements, instead return the head of updated LL.
Input format : Linked list elements (separated by space and terminated by -1)`

Sample Input 1 :
1 4 5 2 -1
Sample Output 1 :
1 5 4 2 
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def arrange_LinkedList(head):
    if head == None:
        return head
    
    odd_head, odd_tail = None, None
    even_head, even_tail = None, None
    
    while head is not None:
        if head.data % 2 == 0 : 
            if even_head == None :
                even_head = head
                even_tail = head
            else:
                even_tail.next = head
                even_tail = head
                
        else:
            if odd_head == None :
                odd_head = head
                odd_tail = head
            else:
                odd_tail.next = head
                odd_tail = head
                
        head = head.next
    
    # corner case 1
    if even_head == None:
        # means that all nodes were odd
        odd_tail = None
        return odd_head
    
    # corner case 2
    if odd_head == None:
        # means that all nodes were even
        even_tail = None
        return even_head
    
    even_tail.next = None
    odd_tail.next = even_head
    return odd_head

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
l = arrange_LinkedList(l)
printll(l)