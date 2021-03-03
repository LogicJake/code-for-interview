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
        pre = 0

        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                result[i] = 1
                pre = i
            else:
                result[i] = result[i - pre] + 1
        return result


# @lc code=end
