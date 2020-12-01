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
            n = len(nums)

            left = 0
            right = n - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:  # 此时第一个相似的一定在mid右边
                    left = mid + 1
                else:
                    right = mid

            return -1 if nums[left] != target else left

        def binarylast(nums, target):
            n = len(nums)

            left = 0
            right = n - 1
            while left < right:
                # 一定要想上取整，否则会死循环，如果right=left+1，不向上取整，mid=left且nums[mid]==target，left=mid，死循环了
                mid = (left + right + 1) // 2
                if nums[mid] > target:  # 此时最后一个相似的一定在mid左边
                    right = mid - 1
                else:
                    left = mid

            return -1 if nums[left] != target else left

        first = binaryfrist(nums, target)
        if first == -1:
            return [-1, -1]

        last = binarylast(nums, target)
        if last == -1:
            return [-1, -1]
        else:
            return [first, last]


# @lc code=end
