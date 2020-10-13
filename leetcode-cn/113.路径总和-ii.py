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
        ans = []
        path = []

        def help(root, target):
            if root is None:
                return

            nonlocal ans

            tmp = target - root.val
            path.append(root.val)

            if tmp == 0 and root.left is None and root.right is None:
                ans.append(path[:])

            help(root.left, tmp)
            help(root.right, tmp)
            path.pop()

        help(root, sum)

        return ans


# @lc code=end
