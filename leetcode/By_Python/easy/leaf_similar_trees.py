# -*- coding: utf-8 -*-
# @Time    : 18-10-25 下午1:14
# @Author  : LogicJake
# @File    : leaf_similar_trees.py


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def get_leaf(self, root):
        res = []
        stack = []
        if root is None:
            return res

        while root is not None or len(stack) != 0:
            while root is not None:
                stack.append(root)
                root = root.left
            if len(stack) != 0:
                root = stack.pop()
                if root.left is None and root.right is None:
                    res.append(root.val)
                root = root.right
        return res

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf1 = self.get_leaf(root1)
        leaf2 = self.get_leaf(root2)
        return leaf1 == leaf2
