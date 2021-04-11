#
# @lc app=leetcode.cn id=1018 lang=python3
#
# [1018] 可被 5 整除的二进制前缀
#

# @lc code=start
from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = []

        num = 0
        for i in A:
            num = num * 2 + i
            ans.append(num % 5 == 0)

        return ans


# @lc code=end
