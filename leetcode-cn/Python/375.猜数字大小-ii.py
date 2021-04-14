#
# @lc app=leetcode.cn id=375 lang=python3
#
# [375] 猜数字大小 II
#


# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for len in range(2, n + 1):
            for start in range(1, n - len + 2):
                min_v = 999999999
                for piv in range(start, start + len - 1):
                    res = piv + max(dp[start][piv - 1],
                                    dp[piv + 1][start + len - 1])
                    min_v = min(min_v, res)

                dp[start][start + len - 1] = min_v

        return dp[1][n]


# @lc code=end
