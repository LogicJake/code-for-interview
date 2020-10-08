#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(
            math.factorial(m + n - 2) / math.factorial(m - 1) /
            math.factorial(n - 1))


# @lc code=end
