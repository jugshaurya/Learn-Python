# https://leetcode.com/problems/longest-common-prefix/solution/
# Watch out the solutions
# - horizontal scanning
# - verticle scanning
# - divide and conquer
# - Binary Search
# - Tries


# O(1) Space | O(nk) time : n->len(strs) and k-> len(longest string in strs)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if(n == 0):
            return ""
        if(n == 1):
            return strs[0]

        max_word = strs[0]
        max_length = len(strs[0])
        for i in range(1, n):
            curr_str = strs[i]
            sub_range = min(len(curr_str), max_length)
            for j in range(sub_range):
                if(curr_str[j] != max_word[j]):
                    max_word = curr_str[:j]
                    max_length = len(max_word)
                    break
            else:
                max_word = curr_str[:sub_range]
                max_length = len(max_word)

        # if all are same return first word
        print(max_word)
        for i in range(n-1):
            if(strs[i] != strs[i+1]):
                return max_word
        else:
            return strs[0]
