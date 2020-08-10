#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
from typing import List


class Solution:
    def binarySearch(self, nums, target):
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = (i + j) // 2

            if nums[mid] < target:
                i += 1
            elif nums[mid] > target:
                j -= 1
            else:
                return mid

        return -1

    def search(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums) - 1 and nums[i] < nums[i + 1]:
            i += 1

        left_res = self.binarySearch(nums[:i + 1], target)

        if left_res != -1:
            return left_res

        right_res = self.binarySearch(nums[i + 1:], target)
        if right_res != -1:
            return i + 1 + right_res
        else:
            return -1


# @lc code=end
