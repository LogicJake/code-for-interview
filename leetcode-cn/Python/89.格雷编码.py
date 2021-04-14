#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res, head = [0], 1
        for _ in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1
        return res


# @lc code=end
