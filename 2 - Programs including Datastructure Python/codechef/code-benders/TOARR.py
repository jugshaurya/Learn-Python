# cook your dish here
def alpha(n, m, arr1, arr2):
    d = {}
    if(n > m):
        big = arr1
        small = arr2
    else:
        big = arr2
        small = arr1

    for i in range(len(big)):
        if(d.get(big[i])):
            d[big[i]] += 1
        else:
            d[big[i]] = 1

    result = []
    for i in range(len(small)):
        if(d.get(small[i]) and d[small[i]] != 0):
            result.append(small[i])
            d[small[i]] -= 1
    return len(result)


t = int(input())
while(t > 0):
    n = int(input())
    arr1 = [int(x) for x in input().split()]
    m = int(input())
    arr2 = [int(x) for x in input().split()]
    print(alpha(n, m, arr1, arr2))
    t -= 1
