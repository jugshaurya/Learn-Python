'''
kReverse
Implement kReverse( int k ) in a linked list i.e. you need to reverse first K elements then reverse next k elements and join the linked list and so on.
Indexing starts from 0. If less than k elements left in the last, you need to reverse them as well. If k is greater than length of LL, reverse the complete LL.
You don't need to print the elements, just return the head of updated LL.
Input format :

Line 1 : Linked list elements (separated by space and terminated by -1)
Line 2 : k
Sample Input 1 :
1 2 3 4 5 6 7 8 9 10 -1
4
Sample Output 1 :
4 3 2 1 8 7 6 5 10 9
Sample Input 2 :
1 2 3 4 5 -1
2
Sample Output 2 :
2 1 4 3 5 
Sample Input 3 :
1 2 3 4 5 6 7 -1
3
Sample Output 3 :
3 2 1 6 5 4 7
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    if head == None or head.next == None:
        return (head, head)
    
    smallhead, smalltail = reverse(head.next)
    smalltail.next = head
    smalltail = head
    smalltail.next = None
    return (smallhead, smalltail)
    
def length(head):
    if head==None:
        return 0
    
    return 1 + length(head.next)
    
def kReverse(head, k) :
    
    if head == None or head.next==None:
        return head
    
    if k >= length(head):
        return reverse(head)[0]
    
    count = 1
    temp_head = head
    temp_tail = head
    while count < k and temp_tail != None :
        count += 1
        temp_tail = temp_tail.next
    
    remaining_head = temp_tail.next
    temp_tail.next = None
    smallhead, smalltail = reverse(temp_head)
    small_list_head = kReverse(remaining_head,k)
    smalltail.next = small_list_head
    return smallhead


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

import sys
sys.setrecursionlimit(11000)
arr=list(int(i) for i in input().split())
l = ll(arr[:-1])
k=int(input())
l = kReverse(l, k)
printll(l)
