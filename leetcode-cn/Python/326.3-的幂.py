#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#

from math import log


# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        a = 3**(int(log(99999999999, 3)))
        return n > 0 and a % n == 0


# @lc code=end
