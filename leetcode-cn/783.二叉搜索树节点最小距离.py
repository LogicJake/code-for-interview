#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
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
