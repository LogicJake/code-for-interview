#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0] * (num + 1)

        i = 0
        b = 1

        while b <= num:
            while i < b and i + b <= num:
                result[i + b] = result[i] + 1
                i += 1

            i = 0
            b = b * 2

        return result


# @lc code=end
