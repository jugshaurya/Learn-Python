'''
Reverse Stack

Reverse a given Stack with the help of another empty stack. Two stacks will be given. Out of which first contains some integers and second one is empty. You need to reverse the first one using second stack. Change in the given first stack itself.
Note : You don't need to print or return the stack, just reverse the given stack and it will be printed internally.
Input format :
Line 1 : Size of Stack
Line 2 : Stack elements (separated by space)
Sample Input 1 :
4 
1 2 3 4     (4 is at top)
Sample Output 1 :
1 2 3 4    (1 is at top)
'''

def reverseStack(s1,s2):
    s3 = []
    while len(s1)!= 0:
        data = s1.pop()
        s2.append(data)

    while len(s2)!= 0:
        data = s2.pop()
        s3.append(data)

    while len(s3)!= 0:
        data = s3.pop()
        s1.append(data)


def reverseStack_recursion(s1,s2):
    
    if s1 == []:
        return 
    top = s1.pop()
    reverseStack_recursion(s1,s2) # using the recusion stack as the third stack
    while len(s1)!= 0:
        data = s1.pop()
        s2.append(data)

    s1.append(top)
    while len(s2)!= 0:
        data = s2.pop()
        s1.append(data)



from sys import setrecursionlimit
setrecursionlimit(11000)

n = int(input())
s1 = [int(ele) for ele in input().split()]
s2 = []

print('Earlier stack was : ', *s1)
reverseStack(s1,s2)
print('After reversing once : ', *s1)
reverseStack_recursion(s1,s2)
print('After reversing once more :', *s1)
