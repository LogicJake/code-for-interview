#!/usr/bin/env python
# coding=UTF-8
'''
@Author: LogicJake
@Date: 2019-03-29 10:32:33
@LastEditTime: 2019-03-29 11:01:10
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    total = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return
        if L <= root.val <= R:
            self.total += root.val
            self.rangeSumBST(root.left, L, R)
            self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            self.rangeSumBST(root.left, L, R)
        elif root.val < L:
            self.rangeSumBST(root.right, L, R)
        return self.total
