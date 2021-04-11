#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

# @lc code=start
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        ans = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                ans[j][i] = matrix[i][j]

        return ans


# @lc code=end
