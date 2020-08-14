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
        result = []
        candidates.sort()
        last_num = -1
        for i, num in enumerate(candidates):
            if num == last_num:
                continue

            last_num = num

            if num < target and i < len(candidates) - 1:
                tmp = self.combinationSum2(candidates[i + 1:], target - num)

                if len(tmp) != 0:
                    for t in tmp:

                        result.append([num] + t)

            elif num == target:
                result.append([num])

        return result


# @lc code=end
