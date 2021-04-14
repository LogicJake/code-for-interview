#
# @lc app=leetcode.cn id=947 lang=python3
#
# [947] 移除最多的同行或同列石头
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dict_X = defaultdict(list)
        dict_Y = defaultdict(list)
        for x, y in stones:
            dict_X[x].append((x, y))
            dict_Y[y].append((x, y))
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            x, y = node
            for i in dict_X[x]:
                dfs(i)
            for i in dict_Y[y]:
                dfs(i)

        ans = 0
        for i in stones:
            i = tuple(i)
            if i not in visited:
                ans += 1
                dfs(i)

        return len(stones) - ans


# @lc code=end
