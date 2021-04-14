#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#


# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False

        if num == 1:
            return True

        for i in [2, 3, 5]:
            if num % i == 0:
                return self.isUgly(num // i)

        return False


# @lc code=end
