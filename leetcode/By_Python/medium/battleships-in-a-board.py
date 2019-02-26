# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-02-26 10:03:22
# @Last Modified time: 2019-02-26 10:43:12


class Solution:

    def countBattleships(self, board) -> int:
        row = len(board)
        column = len(board[0])

        count = 0

        for i in range(row):
            for j in range(column):
                if board[i][j] == 'X':
                    count += 1

                    index = j
                    while index < column:
                        if board[i][index] == 'X':
                            board[i][index] = '-'
                        elif board[i][index] == '.':
                            break
                        index += 1

                    index = i
                    while index < row:
                        if board[index][j] == 'X':
                            board[index][j] = '-'
                        elif board[index][j] == '.':
                            break
                        index += 1
        return count


'''
advantage: just using only O(1) extra memory and without modifying the value of the board

since the ship will be only placed horizontally or vertically,
we only care about whether the left cell is 'X' or the above cell is 'X'
'''


class Solution2:

    def countBattleships(self, board) -> int:
        row = len(board)
        column = len(board[0])

        count = 0

        for i in range(row):
            for j in range(column):
                if board[i][j] == 'X':
                    if (j == 0 or board[i][j - 1] == '.') and (i == 0 or board[i - 1][j] == '.'):
                        count += 1
        return count


if __name__ == '__main__':
    solution = Solution2()

    board = [["X", ".", "X"]]
    solution.countBattleships(board)
