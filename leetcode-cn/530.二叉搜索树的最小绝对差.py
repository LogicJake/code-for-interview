#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        pre = 9999
        ans = 9999

        def help(root):
            if root is None:
                return

            nonlocal ans, pre

            help(root.left)

            val = root.val
            ans = min(ans, abs(val - pre))
            pre = val

            help(root.right)

        help(root)
        return ans


# @lc code=end
