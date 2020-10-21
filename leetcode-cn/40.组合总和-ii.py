#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        path = []
        ans = []

        def help(target, candidates):
            if target == 0:
                ans.append(path[:])

            for i, num in enumerate(candidates):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                if num > target:
                    break

                path.append(num)
                help(target - num, candidates[i + 1:])
                path.pop()

        candidates.sort()
        help(target, candidates)
        return ans


# @lc code=end
