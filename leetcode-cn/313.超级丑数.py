#
# @lc app=leetcode.cn id=313 lang=python3
#
# [313] 超级丑数
#

# @lc code=start
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        kv = [0] * k
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            min_v = 9999999999
            for j in range(k):
                min_v = min(min_v, primes[j] * dp[kv[j]])

            for j in range(k):
                if primes[j] * dp[kv[j]] == min_v:
                    kv[j] += 1

            dp[i] = min_v

        return dp[n - 1]


# @lc code=end
