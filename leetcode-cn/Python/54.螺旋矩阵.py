#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])

        ans = []
        top = 0
        buttom = m - 1
        left = 0
        right = n - 1
        while (left <= right and top <= buttom):
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            for i in range(top + 1, buttom + 1):
                ans.append(matrix[i][right])

            if left < right and top < buttom:
                for i in range(right - 1, left, -1):
                    ans.append(matrix[buttom][i])
                for i in range(buttom, top, -1):
                    ans.append(matrix[i][left])

            left += 1
            right -= 1
            top += 1
            buttom -= 1
        return ans


# @lc code=end
