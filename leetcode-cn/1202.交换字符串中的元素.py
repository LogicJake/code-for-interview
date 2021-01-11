#
# @lc app=leetcode.cn id=1202 lang=python3
#
# [1202] 交换字符串中的元素
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = {i: i for i in range(n)}

        # 并查集
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        # 查找根节点
        for l, r in pairs:
            a, b = find(l), find(r)
            if a != b:
                parent[b] = a

        # 获取根节点对应的连通块集合
        dic = defaultdict(list)
        for i in range(n):
            root = find(i)
            dic[root].append(i)

        # 对每个连通块中元素排序
        res = list(s)
        for k, v in dic.items():
            arr = [s[i] for i in v]
            arr.sort()
            for i in range(len(v)):
                res[v[i]] = arr[i]

        return "".join(res)


# @lc code=end
