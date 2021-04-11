#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#


# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]


# @lc code=end
