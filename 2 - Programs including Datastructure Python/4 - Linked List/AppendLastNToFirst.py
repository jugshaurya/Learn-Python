'''
AppendLastNToFirst

Given a linked list and an integer n, append the last n elements of the LL to front.
Indexing starts from 0. You don't need to print the elements, just update the elements and return the head of updated LL.
Assume given n will be smaller than length of LL.
Input format :

Line 1 : Linked list elements (separated by space and terminated by -1)`

Sample Input 1 :
1 2 3 4 5 -1
3
Sample Output 1 :
3 4 5 1 2

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    if head==None:
        return 0
    
    count = 0
    while head!=None:
        count +=1
        head=head.next
    return count

def append_LinkedList(head,n) :
    start_len = length(head)
    if head == None:
        return head
    
    tail = head
    while tail.next != None:
        tail = tail.next
    
    # making circular list
    tail.next = head
    
    # clearing link from length-n position
    start = start_len - n
    prev = None
    curr = head
    while start>0:
        prev = curr
        curr = curr.next
        start -= 1
    prev.next = None
    head = curr
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

arr=list(int(i) for i in input().split())
l = ll(arr[:-1])
i=int(input())
l = append_LinkedList(l, i)
printll(l)
