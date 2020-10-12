#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        x = None
        y = None
        pre = None

        def help(root):
            nonlocal x, y, pre
            if root is None:
                return

            help(root.left)
            cur = root

            if pre is not None and cur.val < pre.val:
                y = cur
                if x is None:
                    x = pre
                else:
                    return
            pre = cur
            help(root.right)

        help(root)
        x.val, y.val = y.val, x.val


# @lc code=end
