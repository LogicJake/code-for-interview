class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1

        a = 0
        b = 0
        c = 0

        for i in range(2, n):
            n1 = dp[a] * 2
            n2 = dp[b] * 3
            n3 = dp[c] * 5

            dp[i] = min(n1, n2, n3)

            if dp[i] == n1:
                a += 1
            if dp[i] == n2:
                b += 1
            if dp[i] == n3:
                c += 1

        return dp[-1]
        