#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []
        n = len(nums)
        nums.sort()

        def help(candidate):
            if len(path) == n:
                ans.append(path[:])

            pre = -9999
            for i, num in enumerate(candidate):
                if num == pre:
                    continue
                pre = num

                path.append(num)
                new_candidate = []
                for j in range(len(candidate)):
                    if j != i:
                        new_candidate.append(candidate[j])
                help(new_candidate)
                path.pop()

        help(nums)
        return ans


# @lc code=end
