#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def help(root):
            if not root:
                return

            help(root.left)
            result.append(root.val)
            help(root.right)

        help(root)
        return result


# @lc code=end
