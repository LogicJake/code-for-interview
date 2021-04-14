#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for first in range(n - 2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            second = first + 1
            third = n - 1

            if nums[first] > 0:
                continue

            while second < third:
                if nums[first] + nums[second] + nums[third] < 0:
                    second += 1
                elif nums[first] + nums[second] + nums[third] > 0:
                    third -= 1
                else:
                    ans.append([nums[first], nums[second], nums[third]])
                    while second < third and nums[second] == nums[second + 1]:
                        second += 1
                    second += 1

                    while second < third and nums[third] == nums[third - 1]:
                        third -= 1
                    third -= 1

        return ans


# @lc code=end
