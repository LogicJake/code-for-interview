# -*- coding: utf-8 -*-
# @Time    : 18-10-21 下午4:29
# @Author  : LogicJake
# @File    : transpose_matrix.py


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        row = len(A)
        column = len(A[0])
        for i in range(column):
            kk = []
            for j in range(row):
                kk.append(A[j][i])
            res.append(kk)

        return res
