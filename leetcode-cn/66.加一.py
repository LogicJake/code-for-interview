#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + 1
            digits[i] = digits[i] % 10

            if digits[i] != 0:
                return digits

        return [1] + digits


# @lc code=end
