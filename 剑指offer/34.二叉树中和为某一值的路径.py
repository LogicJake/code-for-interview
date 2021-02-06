# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        ans = []
        path = []

        def help(root):
            if not root:
                return

            path.append(root.val)
            if sum(path) == sum_ and root.left is None and root.right is None:
                ans.append(list(path))

            help(root.left)
            help(root.right)
            path.pop()

        help(root)
        return ans
