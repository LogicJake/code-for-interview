#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#


# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b:
            carry = a & b
            a ^= b
            b = ((carry) << 1) & 0xFFFFFFFF
            # print((a, b))
        return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)


# @lc code=end
