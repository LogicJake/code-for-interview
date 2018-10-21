# -*- coding: utf-8 -*-
# @Time    : 18-10-21 下午3:19
# @Author  : LogicJake
# @File    : smallest_range_i.py


class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        max_value = max(A)
        min_value = min(A)

        if max_value - min_value < 2 * K:
            return 0
        else:
            return max_value - min_value - 2 * K


if __name__ == '__main__':
    solution = Solution()
    A = [1, 3, 6]
    K = 3

    res = solution.smallestRangeI(A, K)
    print(res)