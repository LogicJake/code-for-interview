#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []

        def help(root):
            if root is None:
                return

            nodes.append(root)
            help(root.left)
            help(root.right)

        help(root)

        if len(nodes) == 0:
            return

        pre = nodes[0]

        for cur in nodes[1:]:
            pre.left = None
            pre.right = cur

            pre = cur


# @lc code=end
