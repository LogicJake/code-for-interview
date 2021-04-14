#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def helper(self, root, result, path):
#         path.append(str(root.val))

#         if root.left is None and root.right is None:
#             result.append('->'.join(path[:]))

#         if root.left is not None:
#             self.helper(root.left, result, path)

#         if root.right is not None:
#             self.helper(root.right, result, path)

#         path.pop()

#     def binaryTreePaths(self, root: TreeNode) -> List[str]:
#         if root is None:
#             return []

#         result = []
#         path = []
#         self.helper(root, result, path)

#         return result


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []

        result = []
        stack = [(root, str(root.val))]

        while len(stack) != 0:
            node, path = stack.pop()

            if node.left is None and node.right is None:
                result.append(path)

            if node.left is not None:
                stack.append((node.left, path + '->' + str(node.left.val)))

            if node.right is not None:
                stack.append((node.right, path + '->' + str(node.right.val)))

        return result


# @lc code=end
