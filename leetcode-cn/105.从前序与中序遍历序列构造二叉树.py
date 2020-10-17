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
        val_index = {}
        for i, val in enumerate(inorder):
            val_index[val] = i

        def help(left, right):
            if left > right:
                return None

            root_val = preorder.pop(0)
            root = TreeNode(root_val)

            index = val_index[root_val]

            root.left = help(left, index - 1)
            root.right = help(index + 1, right)

            return root

        return help(0, len(inorder) - 1)


# @lc code=end
