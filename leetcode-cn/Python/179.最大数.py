#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = map(str, nums)

        class Compare(str):
            def __lt__(self, s):
                return self + s > s + self

        nums = sorted(nums, key=Compare)

        if nums[0] == '0':
            return '0'

        ans = ''.join(nums)
        return str(ans)


# @lc code=end
