#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        h = len(board)
        w = len(board[0])
        visited = set()

        def find(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            visited.add((i, j))
            result = False
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i <= h - 1 and 0 <= new_j <= w - 1:
                    if (new_i, new_j) not in visited:
                        if find(new_i, new_j, k + 1):
                            result = True
                            break
            visited.remove((i, j))
            return result

        for i in range(h):
            for j in range(w):
                if find(i, j, 0):
                    return True
        return False


# @lc code=end
