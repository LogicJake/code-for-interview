#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_distance = 0
        n = len(nums)

        for i in range(n):
            if i <= max_distance:
                if i + nums[i] > max_distance:
                    max_distance = i + nums[i]

                if max_distance >= n - 1:
                    return True

        return False


# @lc code=end
