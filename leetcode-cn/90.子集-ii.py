#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def help(index):
            ans.append(list(path))

            for i in range(index, len(nums)):
                if i > index and nums[i - 1] == nums[i]:
                    continue

                path.append(nums[i])
                help(i + 1)
                path.pop(-1)

        nums.sort()
        help(0)

        return ans


# @lc code=end
