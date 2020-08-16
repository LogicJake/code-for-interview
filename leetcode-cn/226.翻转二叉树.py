#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root


# @lc code=end
