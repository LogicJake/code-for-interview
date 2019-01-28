# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-28 16:46:20
# @Last Modified time: 2019-01-28 16:52:07


class Solution:

    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        i = len(A) - 1
        while i - 2 >= 0:
            if A[i - 1] + A[i - 2] > A[i]:
                return A[i - 1] + A[i - 2] + A[i]
            i -= 1
        return 0

if __name__ == '__main__':
    solution = Solution()

    A = [3, 6, 2, 3]
    res = solution.largestPerimeter(A)
    print(res)
