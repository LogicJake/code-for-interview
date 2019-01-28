# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-28 14:09:49
# @Last Modified time: 2019-01-28 14:12:39


class Solution:

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        else:
            return self.fib(N - 1) + self.fib(N - 2)
