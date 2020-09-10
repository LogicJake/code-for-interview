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


# from collections import defaultdict

# class Solution:
#     def rob(self, root: TreeNode) -> int:
#         s = defaultdict(int)
#         n = defaultdict(int)
#         def dfs(root):
#             if not root:
#                 return 0
#             dfs(root.left)
#             dfs(root.right)
#             s[root] = root.val + n[root.left] + n[root.right]
#             n[root] = max(n[root.left], s[root.left]) + max(
#                 n[root.right], s[root.right])
#         dfs(root)
#         return max(s[root], n[root])


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return [0, 0]

            ls, ln = dfs(root.left)
            rs, rn = dfs(root.right)

            s = root.val + ln + rn
            n = max(ls, ln) + max(rs, rn)

            return s, n

        s, n = dfs(root)
        return max(s, n)


# @lc code=end
