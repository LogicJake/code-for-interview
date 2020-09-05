#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        level = {}
        max_ll = 0

        queue = [[root, 0]]
        while len(queue) != 0:
            node, ll = queue.pop(0)

            if ll > max_ll:
                max_ll = ll

            if ll not in level:
                level[ll] = [node.val]
            else:
                level[ll].append(node.val)

            if node.left is not None:
                queue.append([node.left, ll + 1])

            if node.right is not None:
                queue.append([node.right, ll + 1])

        result = []
        for i in range(max_ll, -1, -1):
            result.append(level[i])

        return result


# @lc code=end
