#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        stack = []

        def help(root):
            if root is None:
                return

            help(root.left)
            stack.append(root)
            help(root.right)

        help(root)
        sum = 0
        while len(stack) != 0:
            node = stack.pop()
            sum = node.val + sum
            node.val = sum

        return root


# @lc code=end
