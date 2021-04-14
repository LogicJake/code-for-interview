#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#

# @lc code=start
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        ans = 0

        for index in range(len(nums)):
            num = nums[index]

            if num == 0:
                ans = max(ans, cnt)
                cnt = 0
            else:
                cnt += 1
            index += 1

        return max(ans, cnt)


# @lc code=end
