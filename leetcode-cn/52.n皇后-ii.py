#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start


class Solution:
    def totalNQueens(self, n: int) -> int:
        # 已占用的列
        col = []
        # 已占用的主对角线
        main = []
        # 已占用的副对角线
        sub = []
        ans = 0

        def help(i):
            nonlocal ans
            if i == n:
                ans += 1
                return

            for j in range(n):
                if j not in col and i + j not in sub and i - j not in main:
                    col.append(j)
                    main.append(i - j)
                    sub.append(i + j)
                    help(i + 1)
                    col.remove(j)
                    main.remove(i - j)
                    sub.remove(i + j)

        help(0)
        return ans


# @lc code=end
