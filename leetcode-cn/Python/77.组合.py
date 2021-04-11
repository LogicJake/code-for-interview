#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def help(start, k):
            if k == 0 and len(path) == m:
                result.append(path[:])
            for i in range(start, n + 1):
                path.append(i)
                help(i + 1, k - 1)
                path.pop()

        path, result = [], []
        m = k
        help(1, k)

        return result


# @lc code=end
