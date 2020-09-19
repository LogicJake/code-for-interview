#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ans = 0

        def help(root, flag):
            if not root:
                return

            help(root.right, 0)
            help(root.left, 1)

            if flag and not root.right and not root.left:
                self.ans += root.val

        help(root, 0)
        return self.ans


# @lc code=end
