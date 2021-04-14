#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        ans = True

        def help(root):
            if root is None:
                return 0

            nonlocal ans

            left_h = help(root.left)
            if not ans:
                return
            right_h = help(root.right)
            if not ans:
                return

            if abs(left_h - right_h) > 1:
                ans = False

            return max(left_h, right_h) + 1

        help(root)
        return ans


# @lc code=end
