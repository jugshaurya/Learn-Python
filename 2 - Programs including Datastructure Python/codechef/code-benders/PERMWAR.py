# cook your dish here

n = int(input())
arr = [int(x) for x in input().split()]
result = 0
for i in range(n):
    result += (arr[i] % n)
print(result)
