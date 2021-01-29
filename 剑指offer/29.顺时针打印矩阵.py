from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        left = 0
        right = len(matrix[0]) - 1
        top = 0
        button = len(matrix) - 1

        ans = []
        while True:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            if top > button:
                break

            for i in range(top, button + 1):
                ans.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            for i in range(right, left - 1, -1):
                ans.append(matrix[button][i])
            button -= 1
            if top > button:
                break

            for i in range(button, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
            if left > right:
                break

        return ans
