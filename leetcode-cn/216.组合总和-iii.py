#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = list(range(1, 10))
        path = []
        ans = []

        def help(target, candidates):
            if target == 0 and len(path) == k:
                ans.append(path[:])

            for i, num in enumerate(candidates):
                if num > target:
                    break

                path.append(num)
                help(target - num, candidates[i + 1:])
                path.pop()

        help(n, candidates)
        return ans


# @lc code=end
