# -*- coding: utf-8 -*-
# @Time    : 18-10-24 下午1:12
# @Author  : LogicJake
# @File    : maximum_depth_of_n_ary_tree.py


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        if len(root.children) == 0:
            return 1
        return max([self.maxDepth(r) for r in root.children]) + 1
