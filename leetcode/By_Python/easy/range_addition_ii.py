# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-11-10 14:26:46
# @Last Modified time: 2018-11-10 14:55:10


class Solution:

    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        a = m
        b = n
        for op in ops:
            a = min(a, op[0])
            b = min(b, op[1])
        return a * b


if __name__ == '__main__':
    solution = Solution()
    m = 3
    n = 3
    operations = [[2, 2], [3, 3]]
    res = solution.maxCount(m, n, operations)
    print(res)
