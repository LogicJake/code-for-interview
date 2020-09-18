#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
from typing import List


class Solution:
    a = 1

    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []
        n = len(nums)

        def help(candidate):
            if len(path) == n:
                ans.append(path[:])

            for num in candidate:
                path.append(num)
                new_candidate = [n for n in candidate if n != num]
                help(new_candidate)
                path.pop()

        help(nums)
        return ans


# @lc code=end
