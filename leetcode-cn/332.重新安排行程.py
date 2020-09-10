#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#

# @lc code=start
from typing import List
from collections import defaultdict
from heapq import heapify, heappop


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(curr: str):
            while vec[curr]:
                tmp = heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)

        vec = defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            heapify(vec[key])

        stack = list()
        dfs("JFK")
        return stack[::-1]


# @lc code=end
