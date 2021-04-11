#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_loc(nums, target):
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
                else:
                    right = mid

            if left == len(nums) or nums[left] != target:
                return -1

            return left

        def last_loc(nums, target):
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1

            if left == 0 or nums[left - 1] != target:
                return -1

            return left - 1

        first = first_loc(nums, target)

        if first == -1:
            return [-1, -1]

        last = last_loc(nums, target)
        return [first, last]


# @lc code=end
