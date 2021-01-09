#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        queue = ['0000']
        visited = set()
        visited.add('0000')
        depth = 0

        def neighbors(cur):
            res = []
            for i in range(4):
                x = int(cur[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    res.append(cur[:i] + str(y) + cur[i + 1:])

            return res

        while queue:
            sz = len(queue)

            for _ in range(sz):
                cur = queue.pop(0)
                if cur == target:
                    return depth

                for nei in neighbors(cur):
                    if nei not in visited and nei not in deadends:
                        visited.add(nei)
                        queue.append(nei)

            depth += 1

        return -1


# @lc code=end
