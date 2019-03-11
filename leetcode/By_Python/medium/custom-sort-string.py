# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-03-11 12:25:53
# @Last Modified time: 2019-03-11 12:33:41


class Solution:

    def customSortString(self, S: str, T: str) -> str:
        s_set = list(S)

        T_in = []
        T_out = []
        for t in T:
            if t in s_set:
                T_in.append(t)
            else:
                T_out.append(t)
        T_in = sorted(T_in, key=lambda x: s_set.index(x))

        return ''.join(T_in + T_out)


if __name__ == '__main__':
    S = "cba"
    T = "abcd"
    solution = Solution()
    solution.customSortString(S, T)
