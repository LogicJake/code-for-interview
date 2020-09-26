#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
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
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        path = []
        ans = []

        def help(root, num):
            if not root:
                return
            path.append(root.val)

            if num - root.val == 0 and root.right is None and root.left is None:
                ans.append(path[:])

            help(root.left, num - root.val)
            help(root.right, num - root.val)

            path.pop()

        help(root, sum)
        return ans


# @lc code=end
