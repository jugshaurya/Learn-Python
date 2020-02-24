class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if(d.get(nums[i])):
                d[nums[i]] = (d[nums[i]][0] + 1, d[nums[i]][1], i)
            else:
                d[nums[i]] = (1, i, i)

        max_val = -1
        for x, y in d.items():
            max_val = max(max_val, y[0])

        min_length = 9999999
        for x, y in d.items():
            if(y[0] == max_val):
                min_length = min(min_length, y[2]-y[1]+1)

        return min_length
