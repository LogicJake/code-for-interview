# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-12-03 13:37:31
# @Last Modified time: 2018-12-03 13:51:06


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    tilt = 0

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root)
        return self.tilt

    def traverse(self, root):
        if root == None:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.tilt += abs(left - right)
        return left + right + root.val
