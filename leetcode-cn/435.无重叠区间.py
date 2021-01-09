#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)

        if n == 0:
            return 0
            
        end = intervals[0][1]
        ans = 1

        for i in range(1, n):
            if intervals[i][0] >= end:
                ans += 1
                end = intervals[i][1]

        return n - ans


# @lc code=end
