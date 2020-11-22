from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        x_directions = [0, 0, -1, 1]
        y_directions = [-1, 1, 0, 0]

        n = len(board)
        if n == 0:
            return False
        m = len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True

            if not 0 <= i < n or not 0 <= j < m or board[i][j] != word[k]:
                return False

            board[i][j] = ''
            res = False
            for q in range(4):
                if dfs(i + x_directions[q], j + y_directions[q], k + 1):
                    res = True
                    break
            board[i][j] = word[k]

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False
