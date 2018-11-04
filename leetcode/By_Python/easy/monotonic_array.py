# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-11-04 12:40:50
# @Last Modified time: 2018-11-04 13:04:44


class Solution(object):

    def cmp(self, a, b):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        store = 0

        for i in range(len(A) - 1):
            c = self.cmp(A[i], A[i + 1])
            if c:
                if store and c != store:
                    return False
                store = c
        return True

if __name__ == '__main__':
    solution = Solution()

    res = solution.isMonotonic([3, 4, 2, 3])
    print(res)
