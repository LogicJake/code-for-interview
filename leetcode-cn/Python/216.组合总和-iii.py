#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))
        path = []
        ans = []

        def help(nums, target):
            if target == 0 and len(path) == k:
                ans.append(path[:])

            for i, num in enumerate(nums):
                if num > target:
                    break

                path.append(num)
                help(nums[i + 1:], target - num)
                path.pop()

        help(nums, n)
        return ans


# @lc code=end
