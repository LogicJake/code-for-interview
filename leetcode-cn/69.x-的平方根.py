#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#


# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x // 2 + 1

        while left < right:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid
            elif mid * mid == x:
                return mid
            else:
                left = mid + 1

        if left * left > x:
            return left - 1
        return left


# @lc code=end
