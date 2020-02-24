class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n
        for i in range(1, n):
            output[i] = output[i-1] * nums[i-1]

        for_next_time = 1
        for i in range(n-2, -1, -1):
            output[i] *= nums[i+1] * for_next_time
            for_next_time *= nums[i+1]
        return output
