#!/usr/bin/env python
# coding=UTF-8
'''
@Author: LogicJake
@Date: 2019-04-07 20:23:15
@LastEditTime: 2019-04-07 20:34:25
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre, post):
        def fun(pre, post):
            if len(pre) == 0:
                return None
            root = TreeNode(pre[0])
            if len(pre) == 1:
                return root

            index = post.index(pre[1])

            root.left = fun(pre[1:2+index], post[:index+1])
            root.right = fun(pre[2+index:], post[index+1:-1])
            return root
        return fun(pre, post)
