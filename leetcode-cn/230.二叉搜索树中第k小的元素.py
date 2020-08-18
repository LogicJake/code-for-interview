#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, root):
        if root is None:
            return []

        left = self.helper(root.left)
        right = self.helper(root.right)
        return left + [root.val] + right

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        nums = self.helper(root)
        return nums[k - 1]


# @lc code=end
