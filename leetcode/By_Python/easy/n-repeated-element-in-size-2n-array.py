# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-05 14:23:36
# @Last Modified time: 2019-01-05 14:31:55


class Solution:

    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        size = len(A)
        right_mid = size // 2
        left_mid = size // 2 - 1

        A.sort()
        print(right_mid, left_mid)
        if A[right_mid] == A[left_mid]:
            return A[right_mid]
        elif A[right_mid] == A[right_mid + 1]:
            return A[right_mid]
        elif A[left_mid] == A[left_mid - 1]:
            return A[left_mid]

if __name__ == '__main__':
    solution = Solution()
    A = [5, 1, 5, 2, 5, 3, 5, 4]
    res = solution.repeatedNTimes(A)
    print(res)
