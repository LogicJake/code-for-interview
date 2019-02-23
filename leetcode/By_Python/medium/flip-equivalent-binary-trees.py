# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-02-23 13:23:39
# @Last Modified time: 2019-02-23 13:28:13


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        elif root1 and root2 and root1.val == root2.val:
            return True
        else:
            return False

        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.left, root2.right)
                                                                                                         and self.flipEquiv(root1.right, root2.left))
