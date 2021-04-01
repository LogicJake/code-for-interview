#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#


# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) + (n & 1)
            n >>= 1
        return result


# @lc code=end
