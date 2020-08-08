#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
from typing import List
'''
class Solution:
    def threeSum(self, nums, target):
        result = []
        length = len(nums)

        for first in range(length):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            new_target = target - nums[first]

            third = length - 1
            for second in range(first + 1, length):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[
                        third] > new_target:
                    third -= 1

                if second == third:
                    break

                if nums[second] + nums[third] == new_target:
                    result.append([nums[first], nums[second], nums[third]])

        return result

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        nums.sort()
        # 保证有三个数
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            result_part = self.threeSum(nums[i + 1:], target - nums[i])

            for r in result_part:
                result.append([nums[i]] + r)

        return result
'''


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        nums.sort()
        length = len(nums)
        for first in range(0, length - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            for second in range(first + 1, length - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                forth = length - 1
                for third in range(second + 1, length - 1):
                    if third > second + 1 and nums[third] == nums[third - 1]:
                        continue

                    while third < forth and nums[first] + nums[second] + nums[
                            third] + nums[forth] > target:
                        forth -= 1

                    if third == forth:
                        break
                    if nums[first] + nums[second] + nums[third] + nums[
                            forth] == target:
                        result.append([
                            nums[first], nums[second], nums[third], nums[forth]
                        ])
        return result


# @lc code=end
