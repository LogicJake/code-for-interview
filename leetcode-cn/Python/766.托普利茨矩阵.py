#
# @lc app=leetcode.cn id=766 lang=python3
#
# [766] 托普利茨矩阵
#

# @lc code=start
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    continue
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True


# @lc code=end
