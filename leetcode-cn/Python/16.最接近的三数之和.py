#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums, target):
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            new_target = target - nums[first]
            third = len(nums) - 1
            for second in range(first + 1, len(nums)):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                while second < third and nums[second] + nums[
                        third] > new_target:
                    third -= 1

                if second == third:
                    break

                if nums[second] + nums[third] == new_target:
                    return True

        return False

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        diff = 0
        while (1):
            if self.threeSum(nums, target + diff):
                return target + diff

            if self.threeSum(nums, target - diff):
                return target - diff

            diff += 1


# @lc code=end
