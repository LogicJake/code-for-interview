# -*- coding: utf-8 -*-
# @Time    : 18-10-21 下午2:42
# @Author  : LogicJake
# @File    : projection_area_of_3d_shapes.py


class Solution:
    # not good
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for g1 in grid:
            res += max(g1)
            for g2 in g1:
                if g2 != 0:
                    res += 1

        for i in range(len(grid)):
            a = 0
            for g in grid:
                a = max(a, g[i])

            res += a
        return res


if __name__ == '__main__':
    solution = Solution()
    grid = [[1, 2], [3, 4]]

    res = solution.projectionArea(grid)
    print(res)
