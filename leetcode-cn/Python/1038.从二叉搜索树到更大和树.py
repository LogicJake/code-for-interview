#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 从二叉搜索树到更大和树
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    sum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def help(root):
            if root is None:
                return

            help(root.right)
            self.sum += root.val
            root.val = self.sum
            help(root.left)

        help(root)
        return root


# @lc code=end
