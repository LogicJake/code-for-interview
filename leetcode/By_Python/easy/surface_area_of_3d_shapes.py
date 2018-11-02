# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-11-02 13:50:47
# @Last Modified time: 2018-11-02 14:01:51


class Solution(object):

    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        n = len(grid)
        for row in range(n):
            for column in range(n):
                if grid[row][column] != 0:
                    res += 2
                num = grid[row][column]
                if row - 1 >= 0:
                    res += max(0, grid[row][column] - grid[row - 1][column])
                else:
                    res += num

                if row + 1 < n:
                    res += max(0, grid[row][column] - grid[row + 1][column])
                else:
                    res += num

                if column - 1 >= 0:
                    res += max(0, grid[row][column] - grid[row][column - 1])
                else:
                    res += num

                if column + 1 < n:
                    res += max(0, grid[row][column] - grid[row][column + 1])
                else:
                    res += num
        return res

if __name__ == '__main__':
    solution = Solution()

    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    res = solution.surfaceArea(grid)
    print(res)
