
# # Approach 2
# import math
# MAX_SIZE = 100000008
# # MAX_SIZE = 100
# dp = [0]*MAX_SIZE
# for i in range(len(dp)):
#     if(i & 1):
#         dp[i] += 1

# max_digits = math.ceil(math.log(MAX_SIZE, 2))
# for i in range(1, max_digits+1):
#     number_to_add = 0
#     for j in range(1, MAX_SIZE):
#         if(j % pow(2, i) == 0):
#             number_to_add = number_to_add ^ 1
#         dp[j] += number_to_add

# t = int(input())
# while(t > 0):
#     n, q = [int(x) for x in input().split()]
#     arr = [int(x) for x in input().split()]
#     while(q > 0):
#         p = int(input())
#         arrB = [x ^ p for x in arr]  # O(n)
#         binArrB = [(dp[x] & 1) for x in arrB]  # O(n)
#         odd = 0
#         even = 0
#         for ele in binArrB:
#             if(ele == 1):
#                 odd += 1
#             else:
#                 even += 1
#         print(even, odd)
#         q -= 1
#     t -= 1

import math


def count_set_bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


# #  Approac 3
# MAX_SIZE = 100000001
# dp = [0]*MAX_SIZE

# for i in range(1, len(dp)):
#     dp[i] = bin(i).count('1')

# t = int(input())
# while(t > 0):
#     n, q = [int(x) for x in input().split()]
#     arr = [int(x) for x in input().split()]
#     while(q > 0):
#         p = int(input())
#         arrB = [x ^ p for x in arr]  # O(n)
#         binArrB = [dp[x] & 1 for x in arrB]  # O(n)
#         odd = 0
#         even = 0
#         for ele in binArrB:
#             if(ele == 1):
#                 odd += 1
#             else:
#                 even += 1
#         print(even, odd)
#         q -= 1
#     t -= 1


#  Approach 3
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write

t = int(input())


def oddKiEven(x):

    return 0


while(t > 0):
    n, q = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    while(q > 0):
        p = int(input())
        binArrB = [oddKiEven(x) for x in arr]  # O(n)
        odd = 0
        even = 0
        for ele in binArrB:
            if(ele == 1):
                odd += 1
            else:
                even += 1
        print(str(even)+" "+str(odd))
        q -= 1
    t -= 1





    
