#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = 0

        sum_ = 0
        ans = -float('inf')
        while right < len(nums):
            sum_ += nums[right]
            right += 1

            if right - left == k:
                ans = max(ans, sum_ / k)
                sum_ -= nums[left]
                left += 1

        return ans


# @lc code=end
