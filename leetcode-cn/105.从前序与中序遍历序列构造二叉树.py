#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
from typing import List

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        mem = {}

        for index, num in enumerate(inorder):
            mem[num] = index

        def help(left, right):
            if left > right:
                return None

            root_value = preorder.pop(0)
            root = TreeNode(root_value)

            root_index = mem[root_value]
            root.left = help(left, root_index - 1)
            root.right = help(root_index + 1, right)

            return root

        return help(0, len(preorder) - 1)


# @lc code=end
