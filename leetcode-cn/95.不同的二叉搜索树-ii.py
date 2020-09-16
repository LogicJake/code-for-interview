#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []

        def help(start, end):
            if start > end:
                return [None]

            trees = []
            for i in range(start, end + 1):
                ltrees = help(start, i - 1)
                rtrees = help(i + 1, end)

                for ltree in ltrees:
                    for rtree in rtrees:
                        root = TreeNode(i)
                        root.left = ltree
                        root.right = rtree

                        trees.append(root)

            return trees

        return help(1, n)


# @lc code=end
