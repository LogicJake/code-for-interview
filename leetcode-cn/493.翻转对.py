#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
from typing import List
import bisect


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        tb, res = [], 0
        for n in reversed(nums):
            res += bisect.bisect_left(tb, n)
            n2 = 2 * n
            idx = bisect.bisect_left(tb, n2)
            tb.insert(idx, n2)
        return res


# @lc code=end
