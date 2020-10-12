#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#


# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N

        dp = [0] * (N + 1)
        # 进行状态转移
        dp[1] = 1
        for i in range(2, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[N]


# @lc code=end
