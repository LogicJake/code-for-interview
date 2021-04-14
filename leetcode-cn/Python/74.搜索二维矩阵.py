#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        i = 0
        j = m * n

        while i < j:
            mid = (i + j) // 2
            num = matrix[mid // n][mid % n]

            if num < target:
                i = mid + 1
            elif num > target:
                j = mid
            else:
                return True

        return False


# @lc code=end
