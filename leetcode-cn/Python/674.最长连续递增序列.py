#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0
        start = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] <= nums[i - 1]:
                start = i

            ans = max(ans, i - start + 1)

        return ans


# @lc code=end
