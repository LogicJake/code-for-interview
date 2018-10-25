# -*- coding: utf-8 -*-
# @Time    : 18-10-25 下午12:53
# @Author  : LogicJake
# @File    : groups_of_special_equivalent_strings.py


class Solution(object):
    def numSpecialEquivGroups(self, A):
        d = dict()
        for i in A:
            if len(i) >= 2:
                key = (tuple(sorted(i[::2])), tuple(sorted(i[1::2])))
                d[key] = d.get(key, 0) + 1
            else:
                d[i] = d.get(i, 0) + 1
        return len(d)


if __name__ == '__main__':
    solution = Solution()
    A = ["abcd", "cdab", "adcb", "cbad"]
    print(solution.numSpecialEquivGroups(A))
