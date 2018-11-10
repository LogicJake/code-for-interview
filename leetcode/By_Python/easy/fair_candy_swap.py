# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-11-04 13:13:26
# @Last Modified time: 2018-11-10 13:28:49


class Solution(object):

    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sa = sum(A)
        sb = sum(B)
        s = sa - sb
        res = []
        setb = set(B)
        for a in A:
            b = (2 * a - s) / 2
            if b in setb:
                res.append(a)
                res.append(int(b))
                return res

if __name__ == '__main__':
    solution = Solution()
    A = [2]
    B = [1, 3]
    res = solution.fairCandySwap(A, B)
    print(res)
