class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def llinput():
    head = None
    l = [int(x) for x in input().split()]
    l = l[:-1]
    if l==[]:
        return None
    head = Node(l[0])
    tail =  head
    for ele in l[1:]:
        tail.next = Node(ele)
        tail = tail.next

    return head
       
def ithNode(head,i):
    if head== None:
        return None
    
    if i >= length(head):
        return None

    if i == 0:
        return head
    
    return ithNode(head.next, i-1)

def length(head):
    count = 0
    while head is not None:
        count += 1
        head=head.next
    
    return count

def printll(head):
    while head is not None:
        print(head.data,end = ' ')
        head = head.next

    print()

def insert_at_ith(head,i,data):
    if head==None:
        head = Node(data)
        return head
    
    if i>=length(head):
        # add at the tail if i was given wrong
        temp = head
        while temp.next!=None:
            temp=temp.next
        temp.next = Node(data)
        return head

    count = 0 
    curr = head
    prev = None
    while count < i :
        prev = curr
        curr = curr.next
        count += 1

    newNode = Node(data)

    if prev==None:
        newNode.next = head
        head = newNode    
        return head
    prev.next = newNode
    newNode.next = curr
    return head

def insert_at_ith_recusive(head,i,data):
    if head == None:
        head = Node(data)
        return head

    if i==0:
        newNode = Node(data)
        newNode.next = head
        head = newNode
        return head
    
    head.next = insert_at_ith(head.next,i-1,data)
    return head

def delete_ith(head, i):
    if i>=length(head):
        return head
    
    if head==None:
        return 
    if i==0:
        return head.next
    count = 0
    prev = None
    curr = head
    while count < i:
        prev=curr
        curr=curr.next
        count=count+1

    prev.next = curr.next
    return head

def deleteRec(head, i):
    if i>=length(head):
        return head
    
    if head==None:
        return head
    
    if i==0:
        return head.next
    
    smallhead = deleteRec(head.next,i-1)
    head.next = smallhead
    return head
    
import sys
sys.setrecursionlimit(11000)
# give input like 5 4 3 2 1 -1
head = llinput()
print('Your Linked List is: ')
printll(head)
print('Length is :',length(head))
node = ithNode(head, 2)
if node:
    print('Node at 2nd position is : ',end = ' ')
    print(node.data)

head = insert_at_ith(head,0,100)
print('Modified list after inserting : ',end = ' ')
printll(head)

head = delete_ith(head,0)
print('Modified list after deleting : ',end = ' ')
printll(head)