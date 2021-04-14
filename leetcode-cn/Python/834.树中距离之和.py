#
# @lc app=leetcode.cn id=834 lang=python3
#
# [834] 树中距离之和
#

# @lc code=start
from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int,
                             edges: List[List[int]]) -> List[int]:
        dp = [0] * N
        se = [0] * N
        ans = [0] * N
        graph = [[] for _ in range(N)]

        for edge in edges:
            f = edge[0]
            t = edge[1]
            graph[f].append(t)
            graph[t].append(f)

        def dfs(u, f):
            dp[u] = 0
            se[u] = 1

            for v in graph[u]:
                if v == f:
                    continue

                dfs(v, u)
                dp[u] += dp[v] + se[v]
                se[u] += se[v]

        def dfs2(u, f):
            ans[u] = dp[u]

            for v in graph[u]:
                if v == f:
                    continue

                pu = dp[u]
                su = se[u]

                pv = dp[v]
                sv = se[v]

                dp[u] -= se[v] + dp[v]
                se[u] -= se[v]

                dp[v] += se[u] + dp[u]
                se[v] += se[u]

                dfs2(v, u)

                dp[u] = pu
                se[u] = su

                dp[v] = pv
                se[v] = sv

        dfs(0, -1)
        dfs2(0, -1)
        return ans


# @lc code=end
