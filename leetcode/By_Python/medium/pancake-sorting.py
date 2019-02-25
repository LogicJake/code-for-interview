# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-02-25 20:27:29
# @Last Modified time: 2019-02-25 20:54:27


class Solution:

    def pancakeSort(self, A):

        length = len(A)

        res = []
        for i in range(len(A)):
            max_index = A.index(max(A[:length]))
            A = list(reversed(A[:max_index + 1])) + A[max_index + 1:]
            A = list(reversed(A[:length])) + A[length:]
            res.append(max_index + 1)
            res.append(length)
            length -= 1

        return res

if __name__ == '__main__':
    solution = Solution()
    A = [3, 2, 4, 1]
    solution.pancakeSort(A)
