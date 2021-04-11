#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hang_list = [[0] * 9 for _ in range(9)]
        lie_list = [[0] * 9 for _ in range(9)]
        gong_list = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                num = int(board[i][j]) - 1

                if hang_list[i][num] == 1:
                    return False
                else:
                    hang_list[i][num] = 1

                if lie_list[j][num] == 1:
                    return False
                else:
                    lie_list[j][num] = 1

                id = (i // 3) * 3 + (j // 3)
                if gong_list[id][num] == 1:
                    return False
                else:
                    gong_list[id][num] = 1

        return True


# @lc code=end
