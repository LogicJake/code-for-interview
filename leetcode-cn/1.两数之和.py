#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}

        for i, num in enumerate(nums):
            if target - num in mem:
                return [i, mem[target - num]]
            else:
                mem[num] = i


# @lc code=end
