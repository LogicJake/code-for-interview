#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        dp = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])

        ans = []
        path = []

        def help(i):
            if i == n:
                ans.append(path[:])

            for j in range(i, n):
                if dp[i][j]:
                    path.append(s[i:j + 1])
                    help(j + 1)
                    path.pop()

        help(0)
        return ans


# @lc code=end
