# -*- coding: utf-8 -*-
# @Time    : 18-10-20 下午2:20
# @Author  : LogicJake
# @File    : peak_index_in_a_mountain_array.py


class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                return i


if __name__ == '__main__':
    solution = Solution()
    A = [0, 2, 1, 0]
    res = solution.peakIndexInMountainArray(A)
    print(res)
