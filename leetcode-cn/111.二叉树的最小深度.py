#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        left = 9999
        right = 9999
        if root.left is not None:
            left = self.minDepth(root.left)
        if root.right is not None:
            right = self.minDepth(root.right)

        return min(left, right) + 1


# @lc code=end
