#!/usr/bin/env python
# coding=UTF-8
'''
@Author: LogicJake
@Date: 2019-03-29 10:13:21
@LastEditTime: 2019-03-29 11:01:05
'''


class Solution:
    def maxIncreaseKeepingSkyline(self, grid) -> int:
        max_hang = [max(row) for row in grid]

        max_lie = []

        for i in range(len(grid[0])):
            max_ = 0
            for j in range(len(grid)):
                max_ = max(max_, grid[j][i])

            max_lie.append(max_)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(max_hang[i], max_lie[j]) - grid[i][j]
        return res


if __name__ == "__main__":
    solution = Solution()
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    res = solution.maxIncreaseKeepingSkyline(grid)
    print(res)