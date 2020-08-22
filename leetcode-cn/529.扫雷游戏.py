#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
from typing import List


class Solution:
    def dfs(self, board, x, y):
        dir_x = [0, 1, 0, -1, 1, 1, -1, -1]
        dir_y = [1, 0, -1, 0, 1, -1, 1, -1]

        cnt = 0
        for i in range(8):
            xt = x + dir_x[i]
            yt = y + dir_y[i]

            if xt < 0 or yt < 0 or xt >= len(board) or yt >= len(board[0]):
                continue

            if board[xt][yt] == 'M':
                cnt += 1

        if cnt != 0:
            board[x][y] = str(cnt)
        else:
            board[x][y] = 'B'

            for i in range(8):
                xt = x + dir_x[i]
                yt = y + dir_y[i]

                if xt < 0 or yt < 0 or xt >= len(board) or yt >= len(board[0]):
                    continue

                if board[xt][yt] == 'E':
                    self.dfs(board, xt, yt)

    def updateBoard(self, board: List[List[str]],
                    click: List[int]) -> List[List[str]]:
        x, y = click[0], click[1]

        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            self.dfs(board, x, y)

        return board


# @lc code=end
