#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
from typing import List
from collections import defaultdict
# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         citations.sort()

#         n = len(citations)
#         for h in range(n, 0, -1):
#             if citations[n - h] >= h:
#                 return h
#         return 0


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        count = defaultdict(int)
        for c in citations:
            count[min(c, n)] += 1

        s = 0
        for h in range(n, 0, -1):
            s = count[h] + s
            if s >= h:
                return h
        return 0


# @lc code=end
