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
        result = []
        candidates.sort()
        last_num = -1
        for i, num in enumerate(candidates):
            if num == last_num:
                continue

            last_num = num

            if num < target:
                tmp = self.combinationSum(candidates[i:], target - num)

                if len(tmp) != 0:
                    for t in tmp:
                        result.append([num] + t)

            elif num == target:
                result.append([num])

        return result


# @lc code=end
