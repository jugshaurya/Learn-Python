
# give input 1 3 1 4 1 63 1 21 1 9 2 3 1 7 2 2 2 3 -1
''' output should be
3
4
4
63
21
9
'''

from queue_use import QueueUsingArr
q = QueueUsingArr()
li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    if choice == -1: # if choice is -1 break
        break

    elif choice == 1: # if choice is 1 , we take next element to be the data to be inserted inpo queue
        q.enqueue(li[i+1])
        i+=1

    elif choice == 2: # if choice is 2 , we dequeue
        ans = q.dequeue()
        if ans != 0:
            print(ans)
        else:
            print(-1)

    elif choice == 3: # if choice is 3 , we access top
        ans = q.top()
        if ans != 0:
            print(ans)
        else:
            print(-1)

    elif choice == 4: # if choice is 4 , we find the size of Queue
        print(q.size())

    elif choice == 5: # finding if queue is empty or not
        if(q.empty()):
            print('true')
        else:
            print('false')
    i+=1



# -------------------------------------------------------------------------------------------------------------

from queue_using_linkedlist import QueueUsingLL
q = QueueUsingLL()
li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        q.enqueue(li[i+1])
        i+=1
    elif choice == 2:
        ans = q.dequeue()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = q.top()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(q.size())
    elif choice == 5:
        if(q.empty()):
            print('true')
        else:
            print('false')
    i+=1
