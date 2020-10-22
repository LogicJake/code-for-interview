#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        def help(root):
            if not root:
                return 0, 0

            ry, rn = help(root.right)
            ly, ln = help(root.left)

            y = root.val + rn + ln
            n = max(ry, rn) + max(ly, ln)

            return y, n

        return max(help(root))


# @lc code=end
