# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-02-13 20:12:45
# @Last Modified time: 2019-02-13 20:28:48


class Solution:

    def backspaceCompare(self, S: 'str', T: 'str') -> 'bool':

        def build(S):
            res = []
            for c in S:
                if c != '#':
                    res.append(c)
                elif c == '#' and len(res) != 0:
                    res.pop()
            return res

        S = build(list(S))
        T = build(list(T))
        return S == T


class Solution2():

    def backspaceCompare(self, S: 'str', T: 'str') -> 'bool':

        def build(S):
            S.reverse()
            count = 0

            res = []
            for c in S:
                if c == '#':
                    count += 1
                elif count > 0:
                    count -= 1
                else:
                    res.append(c)
            return res

        S = build(list(S))
        T = build(list(T))
        return S == T

if __name__ == '__main__':
    S = "ab##"
    T = "c#d#"
    solution = Solution2()
    solution.backspaceCompare(S, T)
