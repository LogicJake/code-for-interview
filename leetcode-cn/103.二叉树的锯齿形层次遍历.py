#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        level = 0
        ans = []
        queue = []
        if root is None:
            return []
        queue = [root]

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

            if level % 2 == 1:
                nums = nums[::-1]

            ans.append(nums)
            level += 1
        return ans


# @lc code=end
