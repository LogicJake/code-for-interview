# -*- coding: utf-8 -*-
# @Time    : 18-10-24 下午1:09
# @Author  : LogicJake
# @File    : n_ary_tree_postorder_traversal.py


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        stack = []

        if root == None:
            return res
        stack.append(root)
        while len(stack) != 0:
            tmp = stack.pop()
            res.append(tmp.val)
            if len(tmp.children) != 0:
                stack = stack + tmp.children
        res.reverse()
        return res
