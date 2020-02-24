# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def helper(self, root: TreeNode) -> int:
        if(not root):
            return 0
        return min(self.helper(root.left), self.helper(root.right)) + 1

    def minDepth(self, root: TreeNode) -> int:
        return self.helper(root)
