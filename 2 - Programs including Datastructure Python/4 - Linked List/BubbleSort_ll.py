'''
Bubble Sort (Iterative) LinkedList
Sort a given linked list using Bubble Sort (iteratively). While sorting, you need to swap the entire nodes, 
not just the data.
You don't need to print the elements, just sort the elements and return the head of updated LL.
Input format : Linked list elements (separated by space and terminated by -1)
Sample Input 1 :
1 4 5 2 -1
Sample Output 1 :
1 2 4 5
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(head):
    count = 0
    
    while head!=None:
        count+=1
        head=  head.next
        
    return count

def bubbleSortLL(head) :
    if head == None or head.next == None:
        return head
    
    list_len = length(head)
    for i in range(list_len):
        prev = None
        curr = head
        upcoming = curr.next
        while upcoming != None :
            if curr.data <= upcoming.data:
                prev = curr
                curr = curr.next
                upcoming = upcoming.next
            else:
                # swap the nodes
                if prev != None:
                    
                    # changing links
                    prev.next = upcoming
                    curr.next = upcoming.next
                    upcoming.next = curr
                    
                    
                    # updating curr, prev, upcoming for next time
                    prev = prev.next
                    # curr remain same : -> curr = curr
                    upcoming = curr.next
                    
                # if we are swapping the head node
                else:
                    # changing links
                    curr.next = upcoming.next
                    upcoming.next =  curr
                    head = upcoming 
                    
                    # updating curr, prev, upcoming for next time
                    prev = upcoming
                    # curr remain same :-> curr = curr
                    upcoming = curr.next
                    
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
l = bubbleSortLL(l)
printll(l)
