#
# @lc app=leetcode.cn id=1411 lang=python3
#
# [1411] 给 N x 3 网格图涂色的方案数
#


# @lc code=start
class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        fi0, fi1 = 6, 6
        for _ in range(2, n + 1):
            fi0, fi1 = (2 * fi0 + 2 * fi1) % mod, (2 * fi0 + 3 * fi1) % mod
        return (fi0 + fi1) % mod


# @lc code=end
