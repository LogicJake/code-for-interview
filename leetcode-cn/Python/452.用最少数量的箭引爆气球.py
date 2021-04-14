#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        pos = points[0][1]
        ans = 1

        for point in points:
            if point[0] > pos:
                ans += 1
                pos = point[1]

        return ans


# @lc code=end
