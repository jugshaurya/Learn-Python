# Pintu and Fruits Problem Code: CHPINTU - Codechef

t = int(input())
while(t > 0):
    m, baskets = [int(x) for x in input().split()]
    arrF = [int(x) for x in input().split()]
    arrP = [int(x) for x in input().split()]

    d = {}
    for i, fruit in enumerate(arrF):
        if(d.get(fruit)):
            d[fruit] += arrP[i]
        else:
            d[fruit] = arrP[i]

    minEle = min(d, key=d.get)
    print(d[minEle])
    t -= 1
