'''Delete every N nodes
Send Feedback
Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same until end of the linked list. That is, in the given linked list you need to delete N nodes after every M nodes.
Input format :

Line 1 : Linked list elements (separated by space and terminated by -1)
Line 2 : M
Line 3 : N

Sample Input 1 :
1 2 3 4 5 6 7 8 -1
2
2
Sample Output 1 :
1 2 5 6
Sample Input 2 :
1 2 3 4 5 6 7 8 -1
2
3
Sample Output 2 :
1 2 6 7

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def skipMdeleteN(head, M, N):
    
    newhead = head
    newtail = head
    
    head = head.next
    m_count = M - 1 # since 1 is already added to head 
    n_count = N 
    while head != None : 
        if m_count > 0 :
            newtail.next = head 
            newtail = head
            m_count -= 1
        else:
            n_count -= 1
            if n_count == 0:
                m_count = M
                n_count = N
        head = head.next
    
    newtail.next = None
    return newhead
    
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

arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
m=int(input())
n=int(input())
l = skipMdeleteN(l, m, n)
printll(l) 
