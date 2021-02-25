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

        ans = []

        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            third = len(nums) - 1
            target = 0 - nums[first]
            for second in range(first + 1, len(nums)):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                while third > second and nums[second] + nums[third] > target:
                    third -= 1

                if second == third:
                    break

                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans


# @lc code=end
