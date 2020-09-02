#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        change_pos = []

        def helper(board, x, y):
            m = len(board)
            n = len(board[0])
            ax = [-1, 1, 0, 0, -1, -1, 1, 1]
            ay = [0, 0, -1, 1, -1, 1, -1, 1]

            cnt = 0
            for i in range(8):
                if x + ax[i] > -1 and x + ax[i] < m and y + ay[
                        i] > -1 and y + ay[i] < n:
                    if board[x + ax[i]][y + ay[i]] == 1:
                        cnt += 1

            return cnt

        for i in range(len(board)):
            for j in range(len(board[0])):
                cnt = helper(board, i, j)

                if board[i][j] == 1:
                    if cnt < 2:
                        change_pos.append([i, j])
                    elif cnt > 3:
                        change_pos.append([i, j])
                else:
                    if cnt == 3:
                        change_pos.append([i, j])

        for i, j in change_pos:
            board[i][j] = 1 - board[i][j]


# @lc code=end
