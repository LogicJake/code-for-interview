#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
from typing import List


class Solution:
    def helper(self, candidates, target):
        result = []

        last_num = -1
        for i, num in enumerate(candidates):
            if num == last_num:
                continue

            last_num = num

            if num < target and i < len(candidates) - 1:
                tmp = self.helper(candidates[i + 1:], target - num)

                if len(tmp) != 0:
                    for t in tmp:
                        result.append([num] + t)

            elif num == target:
                result.append([num])

        return result

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = list(range(1, 10))
        results = self.helper(candidates, n)
        new_results = []

        for r in results:
            if len(r) == k:
                new_results.append(r)

        return new_results


# @lc code=end
