# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-11-02 12:24:03
# @Last Modified time: 2018-11-02 12:46:02


class Node(object):

    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res = []
        res.append([root.val])
        q = []
        q.append(root)

        while len(q) != 0:
            child_level = []
            num = len(q)
            for i in range(num):
                head = q[0]
                del q[0]
                if len(head.children) != 0:
                    child_val = [c.val for c in head.children]
                    child_level.extend(child_val)
                    q.extend(head.children)

            if len(child_level) != 0:
                res.append(child_level)
        return res
