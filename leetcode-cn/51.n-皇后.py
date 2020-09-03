#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def convert():
            board = []
            for i in range(n):
                row = ['.'] * n
                print(path[i])
                row[path[i]] = 'Q'
                board.append(''.join(row))

            return board

        # 搜索第 i 行
        def dfs(i):
            if i == n:
                result.append(convert())
            else:
                for j in range(n):
                    if j not in col and i - j not in main and i + j not in sub:
                        path.append(j)

                        col.append(j)
                        main.append(i - j)
                        sub.append(i + j)

                        dfs(i + 1)

                        col.remove(j)
                        main.remove(i - j)
                        sub.remove(i + j)
                        path.remove(j)

        result = []
        # 依次存放皇后摆在第几列
        path = []
        # 已占用的列
        col = []
        # 已占用的主对角线
        main = []
        # 已占用的副对角线
        sub = []

        dfs(0)
        return result


# @lc code=end
