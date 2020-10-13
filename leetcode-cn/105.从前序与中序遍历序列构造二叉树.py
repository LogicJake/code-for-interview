#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        node_index = {}
        for i, val in enumerate(inorder):
            node_index[val] = i

        def help(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right or inorder_left > inorder_right:
                return None

            root = TreeNode(preorder[preorder_left])

            root_index = node_index[root.val]

            left_len = root_index - inorder_left

            root.left = help(preorder_left + 1, preorder_left + left_len,
                             inorder_left, root_index - 1)
            root.right = help(preorder_left + left_len + 1, preorder_right,
                              root_index + 1, inorder_right)

            return root

        n = len(preorder)

        return help(0, n - 1, 0, n - 1)


# @lc code=end
