#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]

        def binaryfrist(nums, target):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1

                elif nums[mid] > target:
                    right = mid - 1

            if left == len(nums) or nums[left] != target:
                return -1
            else:
                return left

        def binarylast(nums, target):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1

            if right < 0 or nums[right] != target:
                return -1
            else:
                return right

        first = binaryfrist(nums, target)
        if first == -1:
            return [-1, -1]

        last = binarylast(nums, target)
        return [first, last]


# @lc code=end
