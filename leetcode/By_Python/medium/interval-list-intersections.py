# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-03-11 12:39:01
# @Last Modified time: 2019-03-11 13:13:23


class Interval:

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:

    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        res = []
        for i_a in A:
            for i_b in B:
                if i_a.end < i_b.start:
                    break

                lo = max(i_a.start, i_b.start)
                hi = min(i_a.end, i_b.end)
                if lo <= hi:
                    res.append(Interval(lo, hi))
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.intervalIntersection()
