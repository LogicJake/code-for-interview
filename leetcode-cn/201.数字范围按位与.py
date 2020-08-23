#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#


# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0

        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1

        return m << shift


# @lc code=end
