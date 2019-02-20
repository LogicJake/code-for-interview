# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-02-20 19:03:50
# @Last Modified time: 2019-02-20 21:23:49


class Solution:

    def dailyTemperatures(self, T: 'List[int]') -> 'List[int]':
        next = [float('inf')] * 101
        res = []
        for i in range(len(T) - 1, -1, -1):
            min_index = float('inf')
            for j in range(T[i] + 1, 101):
                if next[j] < min_index:
                    min_index = next[j]
            if min_index < float('inf'):
                res.append(min_index - i)
            else:
                res.append(0)
            next[T[i]] = i
        res.reverse()
        return res


class Solution2:

    def dailyTemperatures(self, T: 'List[int]') -> 'List[int]':
        res = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while len(stack) != 0 and T[i] > T[stack[-1]]:
                index = stack[-1]
                stack = stack[:-1]
                res[index] = i - index
            stack.append(i)
        return res


if __name__ == '__main__':
    solution = Solution2()
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    res = solution.dailyTemperatures(T)
    print(res)
