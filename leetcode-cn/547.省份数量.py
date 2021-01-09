#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0

        citys = list(range(len(isConnected)))
        visited = set()
        for city in citys:
            if city not in visited:
                queue = [city]

                while queue:
                    top = queue.pop(0)
                    visited.add(top)
                    for i in citys:
                        if isConnected[top][i] == 1 and i not in visited:
                            queue.append(i)
                ans += 1

        return ans


# @lc code=end
