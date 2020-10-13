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

        queue = [root]
        ans = []
        while len(queue) != 0:
            sz = len(queue)

            nums = []
            for _ in range(sz):
                node = queue.pop(0)
                nums.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            ans.append(nums)

        ans = ans[::-1]
        return ans


# @lc code=end
