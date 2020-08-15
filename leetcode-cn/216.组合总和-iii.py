#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
from typing import List

# class Solution:
#     def helper(self, candidates, target):
#         result = []

#         last_num = -1
#         for i, num in enumerate(candidates):
#             if num == last_num:
#                 continue

#             last_num = num

#             if num < target and i < len(candidates) - 1:
#                 tmp = self.helper(candidates[i + 1:], target - num)

#                 if len(tmp) != 0:
#                     for t in tmp:
#                         result.append([num] + t)

#             elif num == target:
#                 result.append([num])

#         return result

#     def combinationSum3(self, k: int, n: int) -> List[List[int]]:
#         candidates = list(range(1, 10))
#         results = self.helper(candidates, n)
#         new_results = []

#         for r in results:
#             if len(r) == k:
#                 new_results.append(r)

#         return new_results


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        result = []

        candidates = list(range(1, 10))
        self.dfs(candidates, n, path, result, k)

        new_results = []
        for r in result:
            if len(r) == k:
                new_results.append(r)

        return result

    def dfs(self, candidates, target, path, result, cur):
        if cur < 0:
            return

        if target == 0 and cur == 0:
            result.append(path[:])

        last_num = -1
        for i, num in enumerate(candidates):
            if num == last_num:
                continue

            last_num = num
            new_target = target - num

            if new_target < 0:
                break

            path.append(num)
            self.dfs(candidates[i + 1:], new_target, path, result, cur - 1)
            path.pop()


# @lc code=end
