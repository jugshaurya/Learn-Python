# O(t,n,q) = 4*10^6*5

t = int(input())
while(t):
    n, q = [int(x)for x in input().split()]
    arr = [int(x) for x in input().split()]
    while(q):  # O(q)
        x1, x2, y = [int(x) for x in input().split()]
        leftIndex = x1-1
        rightIndex = x2-1
        count = 0
        # O(rightIndex-leftIndex) = O(max(x1,x2)) = O(N)
        for i in range(leftIndex, rightIndex):
            segmentLeft = arr[i]
            segmentRight = arr[i+1]
            segmentLeftX = i
            segmentRightX = i+1
            small = segmentLeft if segmentLeft < segmentRight else segmentRight
            big = segmentLeft if segmentLeft != small else segmentRight
            # print(small, big)

            if(segmentLeftX != x2-1 and segmentRightX != x1-1 and small <= y and big >= y):
                count += 1
        print(count)
        q -= 1
    t -= 1


# C++


# #include <bits/stdc++.h>
# using namespace std;

# int main() {
#   int t;
#   cin>>t;
#   while(t--){
#     int n,q;
#     cin>>n>>q;
#     int* arr =  new int[n];
#     for (int i=0;i<n;i++){
#       cin>>arr[i];
#     }

#     while(q--){
#       int x1,x2,y;
#       cin>>x1>>x2>>y;
#       int leftIndex = x1-1;
#       int rightIndex = x2-1;
#       int count = 0;
#       // O(rightIndex-leftIndex) = O(max(x1,x2)) = O(N)
#       for (int i = leftIndex; i<rightIndex;i++){

#           int segmentLeft = arr[i];
#           int segmentRight = arr[i+1];
#           int segmentLeftX = i;
#           int segmentRightX = i+1;
#           int small = segmentLeft < segmentRight ? segmentLeft : segmentRight;
#           int big =segmentLeft != small?  segmentLeft: segmentRight;
#           if(segmentLeftX != x2-1 and segmentRightX != x1-1 and small <= y and big >= y){

#               count += 1;
#           }
#       }
#       cout<<count<<endl;
#     }

#     delete[] arr;
#   }
#     return 0;
#   }

# O(t,n,q) = 4*10^6*5

t = int(input())
while(t):
    n, q = [int(x)for x in input().split()]
    arr = [int(x) for x in input().split()]
    while(q):  # O(q)
        x1, x2, y = [int(x) for x in input().split()]
        leftIndex = x1-1
        rightIndex = x2-1
        count = 0
        # O(rightIndex-leftIndex) = O(max(x1,x2)) = O(N)
        for i in range(leftIndex, rightIndex):
            segmentLeft = arr[i]
            segmentRight = arr[i+1]
            segmentLeftX = i
            segmentRightX = i+1
            small = segmentLeft if segmentLeft < segmentRight else segmentRight
            big = segmentLeft if segmentLeft != small else segmentRight
            # print(small, big)

            if(segmentLeftX != x2-1 and segmentRightX != x1-1 and small <= y and big >= y):
                count += 1
        print(count)
        q -= 1
    t -= 1
