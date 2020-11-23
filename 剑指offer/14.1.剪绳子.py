class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], i * (i - j), i * dp[i - j])

        return dp[-1]
