# Leetcode Problem 846


# Complexity: O(n + n*n/w) = O(n^2)
# Space Complexity - extra O(n) for dictionary

from heapq import heappop, heappush, heapify


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        d = {}
        for i in range(len(hand)):  # O(n)
            if(d.get(hand[i])):
                d[hand[i]] += 1
            else:
                d[hand[i]] = 1

        if(len(hand) % W != 0):
            return False

        count = len(hand)
        while(count):  # O(n)
            smallestCard = min(hand)  # O(n/w)
            hand.remove(smallestCard)
            d[smallestCard] -= 1
            for i in range(1, W):
                if(d.get(smallestCard+i) and d.get(smallestCard+i) != 0):
                    d[smallestCard+i] -= 1
                    hand.remove(smallestCard+i)
                else:
                    return False
            count -= W
        return True
