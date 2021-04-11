#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#


# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        i = 1
        while i <= n:
            count += n // (i * 10) * i

            a = n % (i * 10)
            if a >= 2 * i:
                count += i
            elif a >= i:
                count = count + a - i + 1
            i = i * 10

        return count


# @lc code=end
