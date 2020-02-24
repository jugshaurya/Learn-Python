import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -sys.maxsize
        c_sum = 0

        for i in range(len(nums)):
            c_sum += nums[i]
            max_sum = max(max_sum, c_sum)
            if(c_sum < 0):
                c_sum = 0

        return max_sum
