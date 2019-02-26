# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-02-26 11:01:06
# @Last Modified time: 2019-02-26 11:16:54


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def helper(self, nums, left, right):
        if right < left:
            return None
        max_value = max(nums[left:right + 1])
        max_index = nums.index(max_value)

        root = TreeNode(max_value)
        root.left = self.helper(nums, left, max_index - 1)
        root.right = self.helper(nums, max_index + 1, right)

        return root

    def constructMaximumBinaryTree(self, nums):
        root = self.helper(nums, 0, len(nums) - 1)
        return root


if __name__ == '__main__':
    solution = Solution()
    solution.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
