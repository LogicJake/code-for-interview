#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def help(nums, target, left, right):
            i = left
            j = right
            privot = nums[left]
            while i < j:
                while i < j and nums[j] >= privot:
                    j -= 1
                nums[i] = nums[j]

                while i < j and nums[i] <= privot:
                    i += 1
                nums[j] = nums[i]

            if i == target:
                return privot
            elif i < target:
                return help(nums, target, i + 1, right)
            elif i > target:
                return help(nums, target, left, i - 1)

        n = len(nums)
        return help(nums, n - k, 0, len(nums) - 1)


# @lc code=end
