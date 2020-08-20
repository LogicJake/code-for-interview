#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H指数 II
#

# @lc code=start
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        for h in range(n, 0, -1):
            if citations[n - h] >= h:
                return h
        return 0


# @lc code=end
