# -*- coding: utf-8 -*-
# @Time    : 18-10-22 下午2:57
# @Author  : LogicJake
# @File    : n_ary_tree_preorder_traversal.py


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
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
                tmp.children.reverse()
                stack = stack + tmp.children
        return res
