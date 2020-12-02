#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#


# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        def is_prime(x):
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return 0
                i += 1
            return 1

        ans = 0
        for i in range(2, n):
            ans += is_prime(i)
        return ans


# @lc code=end
