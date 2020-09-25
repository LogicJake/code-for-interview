#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while 1:
            g = left + (right - left) // 2
            res = guess(g)

            if res == 0:
                return g
            elif res == -1:
                right = g - 1
            elif res == 1:
                left = g + 1


# @lc code=end
