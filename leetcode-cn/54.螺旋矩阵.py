#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        direction = 0
        ans = []

        def next_pos(i, j, direction):
            # 获取下一个位置
            newi = i
            newj = j
            if direction == 0:
                newi = i
                newj = j + 1
            elif direction == 1:
                newi = i + 1
                newj = j
            elif direction == 2:
                newi = i
                newj = j - 1
            elif direction == 3:
                newi = i - 1
                newj = j

            return newi, newj

        m = len(matrix)
        n = len(matrix[0])

        visited = set()
        i = 0
        j = 0

        while len(ans) != m * n:
            ans.append(matrix[i][j])
            visited.add((i, j))

            newi, newj = next_pos(i, j, direction)
            if (newi, newj
                ) in visited or newi < 0 or newi >= m or newj < 0 or newj >= n:
                direction = (direction + 1) % 4
                i, j = next_pos(i, j, direction)
            else:
                i = newi
                j = newj

        return ans


# @lc code=end
