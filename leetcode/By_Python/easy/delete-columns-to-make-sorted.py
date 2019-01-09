# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-05 18:59:35
# @Last Modified time: 2019-01-05 19:17:31


class Solution:

    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        length = len(A[0])
        pre_c = [a for a in A[0]]

        index = []
        for a in A:
            for i in range(length):
                if i not in index:
                    if a[i] < pre_c[i]:
                        index.append(i)
                    else:
                        pre_c[i] = a[i]
        return len(index)


if __name__ == '__main__':
    solution = Solution()
    A = ["zyx", "wvu", "tsr"]
    solution.minDeletionSize(A)
