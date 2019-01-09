# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-05 15:07:14
# @Last Modified time: 2019-01-05 15:27:57

# Definition for a binary tree node.


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def travel(self, root):
        if root is None:
            return True

        if root.val != self.pre_value:
            return False
        self.pre_value = root.val

        right_res = self.travel(root.right)
        left_res = self.travel(root.left)
        return right_res and left_res

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.pre_value = root.val
        return self.travel(root)
