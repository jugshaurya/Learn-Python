#  O(n^2)
class Solution:
    def trap(self, height: List[int]) -> int:
        total_trapped_water = 0
        for i in range(len(height)):
            max_left, max_right = 0, 0
            #  scope of optimization if precomputions were available
            for j in range(i, -1, -1):
                max_left = max(max_left, height[j])
            for j in range(i, len(height)):
                max_right = max(max_right, height[j])
            mid = min(max_left, max_right)
            if(mid > 0):
                total_trapped_water += (mid - height[i])

        return total_trapped_water

#  O(n)


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0]*n
        max_right = [0]*n

        curr_left_max = 0
        for i in range(n):
            curr_left_max = max(curr_left_max, height[i])
            max_left[i] = curr_left_max

        curr_right_max = 0
        for i in range(n-1, -1, -1):
            curr_right_max = max(curr_right_max, height[i])
            max_right[i] = curr_right_max

        total_trapped_water = 0
        for i in range(len(height)):
            mid = min(max_left[i], max_right[i])
            if(mid > 0):
                total_trapped_water += (mid - height[i])

        return total_trapped_water
