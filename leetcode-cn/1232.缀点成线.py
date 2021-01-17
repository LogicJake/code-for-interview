#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#

# @lc code=start
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(2, len(coordinates)):
            if (coordinates[i][1] - coordinates[1][1]) * (
                    coordinates[1][0] - coordinates[0][0]
            ) != (coordinates[1][1] - coordinates[0][1]) * (coordinates[i][0] -
                                                            coordinates[1][0]):
                return False
        return True


# @lc code=end
