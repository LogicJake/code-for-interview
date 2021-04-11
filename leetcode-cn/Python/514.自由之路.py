#
# @lc app=leetcode.cn id=514 lang=python3
#
# [514] 自由之路
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        pos = defaultdict(list)

        for i, c in enumerate(ring):
            pos[c].append(i)

        m = len(key)
        n = len(ring)

        dp = [[float('inf')] * n for _ in range(m)]
        for i in pos[key[0]]:
            dp[0][i] = min(i, n - i) + 1

        for i in range(1, m):
            for j in pos[key[i]]:
                for k in pos[key[i - 1]]:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - 1][k] + min(abs(j - k), n - abs(j - k)) + 1)

        return min(dp[-1])


# @lc code=end
