#
# @lc app=leetcode.cn id=778 lang=python3
#
# [778] 水位上升的泳池中游泳
#

# @lc code=start
from typing import List


class Dsu:
    def __init__(self, n):
        self.f = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.f[x] == x:
            return x
        else:
            self.f[x] = self.find(self.f[x])
            return self.f[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if self.rank[x] <= self.rank[y]:
            self.f[x] = y
        else:
            self.f[y] = x
        if self.rank[x] == self.rank[y] and x != y:
            self.rank[y] += 1


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        edges = []
        row, col = len(grid), len(grid[0])
        dsu = Dsu(row * col)
        for i in range(row):
            for j in range(col):
                if i < row - 1:
                    edges.append([
                        i * col + j, (i + 1) * col + j,
                        max(grid[i][j], grid[i + 1][j])
                    ])

                if j < col - 1:
                    edges.append([
                        i * col + j, i * col + j + 1,
                        max(grid[i][j], grid[i][j + 1])
                    ])

        edges.sort(key=lambda x: x[-1])
        res = 0
        for edge in edges:
            if dsu.find(edge[0]) != dsu.find(edge[1]):
                dsu.union(edge[0], edge[1])
                res = max(res, edge[-1])
            if dsu.find(0) == dsu.find(col * row - 1):
                break
        return res


# @lc code=end
