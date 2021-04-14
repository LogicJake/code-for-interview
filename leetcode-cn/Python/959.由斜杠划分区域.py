#
# @lc app=leetcode.cn id=959 lang=python3
#
# [959] 由斜杠划分区域
#


# @lc code=start
class UF:
    def __init__(self, M):
        self.parent = {}
        self.cnt = 0
        # 初始化 parent，size 和 cnt
        for i in range(M):
            self.parent[i] = i
            self.cnt += 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return x

    def union(self, p, q):
        if self.connected(p, q):
            return
        leader_p = self.find(p)
        leader_q = self.find(q)
        self.parent[leader_p] = leader_q
        self.cnt -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        N = n * n * 4
        uf = UF(N)

        def get_pos(row, col, i):
            return (row * n + col) * 4 + i

        for row in range(n):
            for col in range(n):
                v = grid[row][col]
                if row > 0:
                    uf.union(get_pos(row - 1, col, 2), get_pos(row, col, 1))
                if col > 0:
                    uf.union(get_pos(row, col - 1, 3), get_pos(row, col, 0))
                if v == '/':
                    uf.union(get_pos(row, col, 0), get_pos(row, col, 1))
                    uf.union(get_pos(row, col, 2), get_pos(row, col, 3))
                if v == '\\':
                    uf.union(get_pos(row, col, 1), get_pos(row, col, 3))
                    uf.union(get_pos(row, col, 0), get_pos(row, col, 2))
                if v == ' ':
                    uf.union(get_pos(row, col, 0), get_pos(row, col, 1))
                    uf.union(get_pos(row, col, 1), get_pos(row, col, 2))
                    uf.union(get_pos(row, col, 2), get_pos(row, col, 3))

        return uf.cnt


# @lc code=end
