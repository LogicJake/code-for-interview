#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#

# @lc code=start
from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)

        dp = [[0] * n for _ in range(m)]

        for i in range(n):
            if B[i] == A[0]:
                dp[0][i] = 1
        for i in range(m):
            if A[i] == B[0]:
                dp[i][0] = 1

        ans = 0
        for i in range(1, m):
            for j in range(1, n):
                if A[i] == B[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
        return ans


# @lc code=end
