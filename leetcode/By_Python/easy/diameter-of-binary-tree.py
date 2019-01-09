# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-12-17 13:17:50
# @Last Modified time: 2018-12-17 13:17:57


class Solution(object):

    def diameterOfBinaryTree(self, root):
        self.ans = 1

        def depth(node):
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L + R + 1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1
