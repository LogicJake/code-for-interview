#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for i in range(numRows):
            row = []

            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ans[-1][j] + ans[-1][j - 1])

            ans.append(row)
        return ans


# @lc code=end
