#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = []
        R = []

        for i in range(len(nums)):
            if i == 0:
                L[0] = 1
            else:
                L[i] = L[i - 1] * nums[i - 1]

        for i in range(len(nums) - 1, -1):
            if i == len(nums) - 1:
                R[i] = 1
            else:
                R[i] = R[i + 1] * nums[R + 1]


# @lc code=end
