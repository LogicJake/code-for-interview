# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-11-04 13:13:26
# @Last Modified time: 2018-11-04 13:33:34


class Solution(object):

    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res = [0, 0]
        for i in range(len(A)):
            for j in range(len(B)):
                res[0] = A[i]
                res[1] = B[j]
                A[i] = res[1]
                B[j] = res[0]

                if sum(A) == sum(B):
                    return res
                else:
                    A[i] = res[0]
                    B[j] = res[1]
