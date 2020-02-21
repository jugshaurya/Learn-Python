
# class Solution:


def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        d[target - nums[i]] = i
    print(d)

    for i, ele in enumerate(nums):
        print(ele)
        if(ele in d and d[ele] != i):
            return [d[ele], i]


twoSum([7, 2, 11, 15], 9)
