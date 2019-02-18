# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-02-18 15:08:25
# @Last Modified time: 2019-02-18 15:32:32


class Solution:

    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        dr = [-1, 0, 1, 0]
        dc = [0, -1, 0, 1]

        R, C = len(grid), len(grid[0])
        queue = list()

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        depth = 0
        while len(queue) != 0:
            r, c, depth = queue.pop(0)
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, depth + 1))

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    return -1
        return depth


if __name__ == '__main__':
    solution = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    solution.orangesRotting(grid)
