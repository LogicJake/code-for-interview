#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def help(root):
            if not root:
                return True, -99999999999, 99999999999

            lres, lmax, lmin = help(root.left)
            rres, rmax, rmin = help(root.right)

            if lres and rres and root.val > lmax and root.val < rmin:
                return True, max(root.val, lmax,
                                 rmax), min(root.val, lmin, rmin)
            else:
                return False, -1, -1

        return help(root)[0]


# @lc code=end
