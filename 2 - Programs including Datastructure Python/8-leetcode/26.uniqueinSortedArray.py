class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        n = len(nums)
        for i in range(1, n):
            if(nums[i] != nums[j]):
                j += 1
                nums[j] = nums[i]
        # print("ara", nums , j)
        return j+1


# def stringToIntegerList(input):
#     return json.loads(input)


# def integerListToString(nums, len_of_list=None):
#     if not len_of_list:
#         len_of_list = len(nums)
#     return json.dumps(nums[:len_of_list])


# def main():
#     import sys
#     import io

#     def readlines():
#         for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
#             yield line.strip('\n')

#     lines = readlines()
#     while True:
#         try:
#             line = next(lines)
#             nums = stringToIntegerList(line)

#             ret = Solution().removeDuplicates(nums)

#             out = integerListToString(nums, len_of_list=ret)
#             print(out)
#         except StopIteration:
#             break


# if __name__ == '__main__':
#     main()
