class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        # assumkinh i and j are given within limits
def swap_nodes(head, i, j):
    if head==None or i>=j:
        return head

    # let's first reach out at the previous of i th and jth nodes ,and now i < j
    ith_prev, jth_prev = None, None
    temp = head
    while j > 0 : # as j is bigger always
        if i > 0 :
            ith_prev = temp
        
        if j > 0 :
            jth_prev = temp
        
        i -= 1
        j -= 1
        temp = temp.next
        
    # now i and j -th pointers are at their correct position
    # swapping nodes
    if ith_prev != None :  # means i is not 0
        # saving some pointers
        ith_node = ith_prev.next
        jth_node = jth_prev.next
        jth_next = jth_node.next
        
        # making changes
        ith_prev.next = jth_node
        jth_node.next = ith_node.next
        jth_prev.next = ith_node
        ith_node.next = jth_next 
    
    else: # ith is at head
        # saving some pointers
        ith_node = ith_prev.next        
        ith_next = ith_node.next
        jth_node = jth_prev.next        
        jth_next = jth_node.next
            
        # making changes    
        head = jth_node
        jth_node.next = ith_next
        jth_prev.next = ith_node
        ith_node.next = jth_next

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
i, j=list(int(i) for i in input().split())
l = swap_nodes(l, i, j)
printll(l)
