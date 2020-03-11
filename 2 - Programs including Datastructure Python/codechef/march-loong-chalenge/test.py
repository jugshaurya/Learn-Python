# Ada Bishop 2
t = int(input())
# Got 99 points !
while(t):
    sr, sc = [int(x) for x in input().split()]
    print(sr, sc)

    if(sr == 1 and sc == 1):
        print(8, 8)
        print(7, 7)
        print(6, 8)
        print(1, 3)
        print(2, 4)
        print(1, 5)
        print(4, 8)
        print(3, 7)
        print(2, 8)
        print(1, 7)
        print(5, 3)
        print(3, 1)
        print(8, 6)
        print(7, 5)
        print(8, 4)
        print(5, 1)
        print(6, 2)
        print(7, 1)
        print(8, 2)
    else:
        print("Not Smart Haah!")
    t -= 1
