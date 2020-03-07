#  Not completely solved

x, y = [int(a) for a in input().split()]
if(x < 2):
    x = 2


def isrep(bini):
    n = len(bini)
    if((n//2) & 1):
        mid = n//2
    else:
        mid = n//2 - 1
    for j in range(n//2):
        if(bini[j] != bini[j + mid]):
            return False

    return True


def getCount(s, e):
    if(s > e):
        return 0
    if(s == e):
        return 1 if isrep(bin(s)[2:]) else 0
    mid = (s+e)//2
    return getCount(s, mid) + getCount(mid+1, e)


print(getCount(x, y+1))
