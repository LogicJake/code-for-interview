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
        if not preorder:
            return None

        root_val = preorder[0]
        root_index = inorder.index(root_val)
        root = TreeNode(root_val)

        root.left = self.buildTree(preorder[1:root_index + 1],
                                   inorder[:root_index])
        root.right = self.buildTree(preorder[root_index + 1:],
                                    inorder[root_index + 1:])

        return root


# @lc code=end
