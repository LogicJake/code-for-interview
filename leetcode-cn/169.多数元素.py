#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = None
        cnt = 0

        for num in nums:
            if cnt == 0:
                ans = num

            if num == ans:
                cnt += 1
            else:
                cnt -= 1

        return ans


# @lc code=end
