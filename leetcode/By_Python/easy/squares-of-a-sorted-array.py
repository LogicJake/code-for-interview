# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-26 14:59:02
# @Last Modified time: 2019-01-26 15:23:55


class Solution:

    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(A) - 1

        res = [0 for i in range(len(A))]
        index = len(A) - 1
        while i < len(A) and j > -1 and i <= j:
            if abs(A[i]) > abs(A[j]):
                res[index] = A[i] * A[i]
                index -= 1
                i += 1
            else:
                res[index] = A[j] * A[j]
                index -= 1
                j -= 1

        return res
