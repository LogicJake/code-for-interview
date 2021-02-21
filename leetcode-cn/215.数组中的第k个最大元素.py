#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(nums, left, right, k):
            if left >= right:
                return nums[left]

            privot = nums[left]

            i = left
            j = right

            while i < j:
                while i < j and nums[j] >= privot:
                    j -= 1
                nums[i] = nums[j]

                while i < j and nums[i] <= privot:
                    i += 1
                nums[j] = nums[i]

            if i == k:
                return privot
            elif k < i:
                return quick_sort(nums, left, i - 1, k)
            else:
                return quick_sort(nums, i + 1, right, k)

        return quick_sort(nums, 0, len(nums) - 1, len(nums) - k)


# @lc code=end
