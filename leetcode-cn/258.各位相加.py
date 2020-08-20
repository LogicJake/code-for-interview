#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#


# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            t = 0
            while num > 0:
                t += num % 10
                num = num // 10
            num = t

        return num


# @lc code=end
