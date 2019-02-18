# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-02-18 15:32:39
# @Last Modified time: 2019-02-18 15:51:16


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = {}

    def depth(self, root, depth, x, y, par):
        if root.val == x:
            self.res[x] = [par, depth]
        if root.val == y:
            self.res[y] = [par, depth]

        if root.left is not None:
            self.depth(root.left, depth + 1, x, y, root)
        if root.right is not None:
            self.depth(root.right, depth + 1, x, y, root)

    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        self.depth(root, 0, x, y, None)
        if self.res[x][0] != self.res[y][0] and self.res[x][1] == self.res[y][1]:
            return True
        return False
