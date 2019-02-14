# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-02-13 18:54:19
# @Last Modified time: 2019-02-13 19:21:01


class SolutionTry:
    # high memory and long time

    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        A.reverse()

        num = 0
        for index, i in enumerate(A):
            num += i * 10**index

        num += K

        res = []
        if num == 0:
            return [0]
        while num != 0:
            res.append(num % 10)
            num //= 10
        res.reverse()
        return res


class Solution:

    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        A.reverse()
        K_list = []

        while K != 0:
            K_list.append(K % 10)
            K //= 10

        if len(K_list) == 0:
            K_list = [0]

        res = []

        flag = 0
        i = 0
        while i < len(A) and i < len(K_list):
            add = A[i] + K_list[i] + flag
            res.append(add % 10)
            flag = add // 10
            i += 1

        while i < len(A):
            add = A[i] + flag
            res.append(add % 10)
            flag = add // 10
            i += 1

        while i < len(K_list):
            add = K_list[i] + flag
            res.append(add % 10)
            flag = add // 10
            i += 1

        if flag == 1:
            res.append(flag)
        res.reverse()
        return res

if __name__ == '__main__':
    A = [0]
    K = 0

    solution = Solution()
    solution.addToArrayForm(A, K)
