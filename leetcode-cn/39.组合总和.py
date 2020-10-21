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
        path = []
        ans = []
        candidates.sort()

        def help(target, candidates):
            if target == 0:
                ans.append(path[:])

            for i, num in enumerate(candidates):
                if num > target:
                    break
                path.append(num)
                help(target - num, candidates[i:])
                path.pop()

        help(target, candidates)
        return ans


# @lc code=end
