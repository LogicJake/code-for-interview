#
# @lc app=leetcode.cn id=1319 lang=python3
#
# [1319] 连通网络的操作次数
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        edges = defaultdict(list)
        for x, y in connections:
            edges[x].append(y)
            edges[y].append(x)

        seen = set()

        def dfs(u: int):
            seen.add(u)
            for v in edges[u]:
                if v not in seen:
                    dfs(v)

        ans = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1

        return ans - 1


# @lc code=end
