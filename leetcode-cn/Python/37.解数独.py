#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        line = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        valid = False
        spaces = []

        def dfs(index):
            nonlocal valid
            if index == len(spaces):
                valid = True
                return

            i, j = spaces[index]
            for digit in range(9):
                if not line[i][digit] and not column[j][digit] and not block[
                        i // 3][j // 3][digit]:
                    line[i][digit] = True
                    column[j][digit] = True
                    block[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(index + 1)
                    line[i][digit] = False
                    column[j][digit] = False
                    block[i // 3][j // 3][digit] = False

                if valid:
                    return

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    line[i][digit] = True
                    column[j][digit] = True
                    block[i // 3][j // 3][digit] = True

        dfs(0)


# @lc code=end
