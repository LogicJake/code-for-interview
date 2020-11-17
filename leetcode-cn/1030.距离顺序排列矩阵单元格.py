#
# @lc app=leetcode.cn id=1030 lang=python3
#
# [1030] 距离顺序排列矩阵单元格
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int,
                          c0: int) -> List[List[int]]:
        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        bucket = defaultdict(list)

        def dist(r1, c1, r2, c2):
            return abs(r1 - r2) + abs(c1 - c2)

        for i in range(R):
            for j in range(C):
                bucket[dist(i, j, r0, c0)].append([i, j])

        ret = list()
        for i in range(maxDist + 1):
            ret += (bucket[i])

        return ret


# @lc code=end
