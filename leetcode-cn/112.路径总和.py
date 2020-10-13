#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        ans = False

        def help(root, target):
            if root is None:
                return

            nonlocal ans

            tmp = target - root.val

            if tmp == 0 and root.left is None and root.right is None:
                ans = True

            help(root.left, tmp)
            help(root.right, tmp)

        help(root, sum)

        return ans


# @lc code=end
