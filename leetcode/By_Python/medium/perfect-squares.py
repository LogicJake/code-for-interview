# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-03-16 16:54:46
# @Last Modified time: 2019-03-16 17:34:11


class Solution:

    def numSquares(self, n: int) -> int:
        r = [0]

        for i in range(1, n + 1):
            r.append(min(r[i - index * index]
                         for index in range(1, int((i + 1)**0.5 + 1))) + 1)
        return r[-1]

if __name__ == '__main__':
    solution = Solution()
    res = solution.numSquares(7927)
