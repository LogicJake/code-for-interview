#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        ans = []
        path = []
        candidates.sort()

        def help(candidates, t):
            if t == 0:
                ans.append(path[:])
                return

            for i, num in enumerate(candidates):
                if num > t:
                    break
                path.append(num)
                help(candidates[i:], t - num)
                path.pop()

        help(candidates, target)

        return ans


# @lc code=end
