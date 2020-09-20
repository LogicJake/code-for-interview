#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path = []
        ans = []

        def help(index):
            ans.append(path[:])

            for i in range(index, len(nums)):
                path.append(nums[i])
                help(i + 1)
                path.pop()

        help(0)
        return ans


# @lc code=end
