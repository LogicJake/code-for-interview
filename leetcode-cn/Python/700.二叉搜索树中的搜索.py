#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def help(root):
            if not root:
                return None

            if root.val == val:
                return root
            elif val < root.val:
                return help(root.left)
            else:
                return help(root.right)

        return help(root)


# @lc code=end
