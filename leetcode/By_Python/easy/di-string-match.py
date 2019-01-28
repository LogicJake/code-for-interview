# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-26 17:51:41
# @Last Modified time: 2019-01-26 17:57:31


class Solution:

    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        min_value = 0
        max_value = len(S)
        for c in S:
            if c == 'I':
                res.append(min_value)
                min_value += 1
            else:
                res.append(max_value)
                max_value -= 1
        res.append(min_value)
        return res
