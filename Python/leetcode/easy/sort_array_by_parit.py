# -*- coding: utf-8 -*-
# @Time    : 18-10-20 下午12:33
# @Author  : LogicJake
# @File    : sort_array_by_parit.py


class Solution:

    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        for i in A:
            if i % 2 == 0:
                res.insert(0, i)
            else:
                res.append(i)
        return res

    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        even = 0
        odd = 1
        for i in A:
            if i % 2 == 0:
                res.insert(even, i)
                even += 2
            else:
                res.insert(odd, i)
                odd += 2
        return res


if __name__ == '__main__':
    solution = Solution()
    A = [4,2,5,7]

    solution.sortArrayByParityII(A)
