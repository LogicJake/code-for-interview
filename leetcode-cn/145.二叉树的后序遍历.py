#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     path = []

    #     def help(root):
    #         if not root:
    #             return

    #         help(root.left)
    #         help(root.right)
    #         path.append(root.val)

    #     help(root)
    #     return path

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        path = []
        stack = []
        prev = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if not root.right or root.right == prev:
                path.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return path


# @lc code=end
