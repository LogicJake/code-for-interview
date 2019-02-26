# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-02-26 11:26:55
# @Last Modified time: 2019-02-26 12:40:26


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

    def helper_insert(self, root, direction, num):
        if not root:
            return
        num_insert = root.val
        index = self.nums.index(num)
        if direction:
            self.nums.insert(index, num_insert)
        else:
            self.nums.insert(index + 1, num_insert)

        self.helper_insert(root.left, True, num_insert)
        self.helper_insert(root.right, False, num_insert)

    def insertIntoMaxTree(self, root, val):
        num = root.val
        self.nums = [num]
        self.helper_insert(root.left, True, num)
        self.helper_insert(root.right, False, num)
        self.nums.append(val)

        return self.constructMaximumBinaryTree(self.nums)
