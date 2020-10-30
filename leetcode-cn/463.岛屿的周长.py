#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions_x = [0, -1, 0, 1]
        directions_y = [-1, 0, 1, 0]

        m = len(grid)

        if m == 0:
            return 0

        n = len(grid[0])

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                for index in range(4):
                    new_x = i + directions_x[index]
                    new_y = j + directions_y[index]

                    if new_x < 0 or new_x >= m:
                        ans += 1
                        continue

                    if new_y < 0 or new_y >= n:
                        ans += 1
                        continue

                    if grid[new_x][new_y] == 0:
                        ans += 1

        return ans


# @lc code=end
