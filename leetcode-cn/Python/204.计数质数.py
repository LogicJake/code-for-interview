#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#


# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [1] * n
        ans = 0

        for i in range(2, n):
            if prime[i] == 1:
                ans += 1

                s = i * i
                while s < n:
                    prime[s] = 0
                    s += i
        return ans


# @lc code=end
