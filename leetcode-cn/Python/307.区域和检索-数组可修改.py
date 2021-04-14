#
# @lc app=leetcode.cn id=307 lang=python3
#
# [307] 区域和检索 - 数组可修改
#
from typing import List


# @lc code=start
class NumArray:
    def __init__(self, nums: List[int]):
        sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            sums[i + 1] = sums[i] + nums[i]

        self.sums = sums
        self.nums = nums

    def update(self, i: int, val: int) -> None:
        diff = val - self.nums[i]
        self.nums[i] = val
        for j in range(i + 1, len(self.sums)):
            self.sums[j] = self.sums[j] + diff

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
# @lc code=end
