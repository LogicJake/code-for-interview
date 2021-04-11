#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        ans = 0
        path = []

        def help(root):
            nonlocal ans
            path.append(root.val)

            if not root.left and not root.right:
                tmp = 0
                for i, num in enumerate(path[::-1]):
                    tmp += num * 10**i
                ans += tmp

            if root.left:
                help(root.left)

            if root.right:
                help(root.right)

            path.pop()

        help(root)
        return ans


# @lc code=end
