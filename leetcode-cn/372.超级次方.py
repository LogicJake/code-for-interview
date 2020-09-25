#
# @lc app=leetcode.cn id=372 lang=python3
#
# [372] 超级次方
#

# @lc code=start
from typing import List


class Solution:
    base = 1337

    def pow(self, a, k):
        if k == 0:
            return 1
        a = a % self.base

        if k % 2 == 0:
            tmp = self.pow(a, k // 2)
            return (tmp * tmp) % self.base
        else:
            tmp = self.pow(a, k - 1)
            return (tmp * a) % self.base

    def superPow(self, a: int, b: List[int]) -> int:
        if len(b) == 0:
            return 1

        last = b.pop()

        part1 = self.pow(a, last)
        part2 = self.pow(self.superPow(a, b), 10)

        return (part1 * part2) % self.base


# @lc code=end
