#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def help(left, right):
            nonlocal map_dict
            if left > right:
                return None

            val = postorder.pop()
            node = TreeNode(val)
            index = map_dict[val]

            node.right = help(index + 1, right)
            node.left = help(left, index - 1)
            return node

        map_dict = {val: index for index, val in enumerate(inorder)}
        root = help(0, len(inorder) - 1)
        return root


# @lc code=end
