from typing import List


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        ans = []

        dp = [[0 for _ in range(6 * n + 1)] for _ in range(n + 1)]

        for i in range(1, 7):
            dp[1][i] = 1

        for i in range(2, n + 1):
            for j in range(i, i * 6 + 1):
                for k in range(1, 7):
                    if j - k > 0:
                        dp[i][j] += dp[i - 1][j - k]
                    else:
                        break

        for i in range(n, 6 * n + 1):
            ans.append(dp[n][i] * pow(1 / 6, n))

        return ans
