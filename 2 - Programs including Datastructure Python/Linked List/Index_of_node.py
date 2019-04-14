'''
Find a node in LL (recursive)
Given a linked list and an integer n you need to find and return index where n is present in the LL. Do this recursively.
Return -1 if n is not present in the LL.
Indexing of nodes starts from 0.
Input format :
Line 1 : Linked list elements (separated by space and terminated by -1)
Line 2 : Integer n 
Output format :
Index
Sample Input 1 :
3 4 5 2 6 1 9 -1
5
Sample Output 1 :
2
'''

class Node:


    def __init__(self, data):
        self.data = data
        self.next = None

def linearSearchRecursive(head, n):
    
    if head == None:
        return -1
    
    if head.data == n:
        return 0
    
    smallIndex = linearSearchRecursive(head.next,n)
    if smallIndex == -1:
        return -1
    return 1 + smallIndex
    
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

from sys import setrecursionlimit
setrecursionlimit(11000)
arr=list(int(i) for i in input().split())
l = ll(arr[:-1])
data=int(input())
index = linearSearchRecursive(l, data)
print(index)
