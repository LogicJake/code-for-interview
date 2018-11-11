# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-11-11 13:50:55
# @Last Modified time: 2018-11-11 14:28:07


class Node:

    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:

    def list_sum(self, aa):
        sums = [sum(a) for a in aa]
        return sum(sums)

    def construct_node(self, grid, n):
        node = None
        if self.list_sum(grid) == n * n // 4:
            node = Node(True, True, None, None, None, None)
        elif self.list_sum(grid) == 0:
            node = Node(False, True, None, None, None, None)
        else:
            node = self.construct(grid)
        return node

    def construct(self, grid):
        """
        : type grid: List[List[int]]
        : rtype: Node
        """
        n = len(grid)

        if self.list_sum(grid) == n * n:
            return Node(True, True, None, None, None, None)
        if self.list_sum(grid) == 0:
            return Node(False, True, None, None, None, None)

        top = grid[0:n // 2]
        grid_top_left = [g[0:n // 2] for g in top]
        grid_top_right = [g[n // 2:] for g in top]
        button = grid[n // 2:]
        grid_buttom_left = [g[0:n // 2] for g in button]
        grid_buttom_right = [g[n // 2:] for g in button]

        top_left = self.construct_node(grid_top_left, n)
        top_right = self.construct_node(grid_top_right, n)
        buttom_left = self.construct_node(grid_buttom_left, n)
        buttom_right = self.construct_node(grid_buttom_right, n)

        root = Node(True, False, top_left, top_right,
                    buttom_left, buttom_right)
        return root

if __name__ == '__main__':
    solution = Solution()
    grid = [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [
        1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]
    res = solution.construct(grid)
    print(res)
