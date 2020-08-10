#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
from typing import List


class Solution:
    '''
    def quickSort(self, nums, left, right):
        if right - left <= 0:
            return

        tmp = nums[left]

        i = left
        j = right

        while i < j:
            while nums[j] > tmp and i < j:
                j -= 1

            while nums[i] <= tmp and i < j:
                i += 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[i] = nums[i], nums[left]

        self.quickSort(nums, left, i - 1)
        self.quickSort(nums, i + 1, right)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 快排
        self.quickSort(nums, 0, len(nums) - 1)
        return nums[len(nums) - k]
    '''
    def quickSearch(self, nums, left, right):
        if self.find:
            return

        if right - left <= 0:
            self.k_max = nums[left]
            self.find = True

        tmp = nums[left]

        i = left
        j = right

        while i < j:
            while nums[j] > tmp and i < j:
                j -= 1

            while nums[i] <= tmp and i < j:
                i += 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[i] = nums[i], nums[left]

        if i == self.k:
            self.k_max = nums[i]
            self.find = True
        elif i > self.k:
            self.quickSearch(nums, left, i - 1)
        else:
            self.quickSearch(nums, i + 1, right)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.find = False
        self.k_max = None
        self.k = len(nums) - k
        self.quickSearch(nums, 0, len(nums) - 1)
        return self.k_max


# @lc code=end
