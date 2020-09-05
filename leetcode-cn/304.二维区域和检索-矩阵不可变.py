#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#

# @lc code=start
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # 行
        m = len(matrix)
        # 列
        if m == 0:
            return

        n = len(matrix[0])

        sums = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            for j in range(m):
                if j == 0:
                    sums[j][i] = sum([matrix[0][a] for a in range(i + 1)])
                else:
                    sums[j][i] = sums[j - 1][i] + sum(
                        [matrix[j][a] for a in range(0, i + 1)])
        self.sums = sums

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left_up = [row1, col1]
        right_up = [row1, col2]

        left_down = [row2, col1]
        right_down = [row2, col2]

        part1 = self.sums[right_down[0]][right_down[1]]
        part2 = 0 if right_up[0] == 0 else self.sums[right_up[0] -
                                                     1][right_up[1]]
        part3 = 0 if left_down[1] == 0 else self.sums[left_down[0]][
            left_down[1] - 1]
        part4 = 0 if left_up[1] == 0 or left_up[0] == 0 else self.sums[
            left_up[0] - 1][left_up[1] - 1]

        return part1 - part2 - part3 + part4


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end
