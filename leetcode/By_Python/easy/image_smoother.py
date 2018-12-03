# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-11-27 12:39:47
# @Last Modified time: 2018-11-27 12:56:41
from math import floor


class Solution:

    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(M)
        column = len(M[0])

        res = [0] * column
        res = [res.copy() for i in range(row)]

        for i in range(row):
            for j in range(column):
                total = 0
                num = 0
                if j + 1 != column:
                    if i + 1 != row:
                        num += 1
                        total += M[i + 1][j + 1]
                    if i - 1 >= 0:
                        num += 1
                        total += M[i - 1][j + 1]
                    num += 1
                    total += M[i][j + 1]
                if j - 1 >= 0:
                    if i + 1 != row:
                        num += 1
                        total += M[i + 1][j - 1]
                    if i - 1 >= 0:
                        num += 1
                        total += M[i - 1][j - 1]
                    num += 1
                    total += M[i][j - 1]
                if i + 1 != row:
                    num += 1
                    total += M[i + 1][j]
                if i - 1 >= 0:
                    num += 1
                    total += M[i - 1][j]
                num += 1
                total += M[i][j]
                res[i][j] = floor(total / num)
        return res


if __name__ == '__main__':
    solution = Solution()
    M = [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]
    res = solution.imageSmoother(M)
    print(res)
