#
# @lc app=leetcode.cn id=218 lang=python3
#
# [218] 天际线问题
#

# @lc code=start
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        all_points = []
        for building in buildings:
            all_points.append((building[0], -building[2]))
            all_points.append((building[1], building[2]))

        all_points.sort()

        heights = []
        result = []
        heights.append(0)

        for x, h in all_points:
            if h < 0:
                h = -h
                max_height = max(heights)
                if h > max_height:
                    result.append([x, h])
                heights.append(h)
            else:
                before_max_height = max(heights)
                heights.remove(h)
                after_max_height = max(heights)
                if after_max_height != before_max_height:
                    result.append([x, after_max_height])

        return result


# @lc code=end
