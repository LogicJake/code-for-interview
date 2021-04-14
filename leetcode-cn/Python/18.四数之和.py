#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue

                left = j + 1
                right = len(nums) - 1
                tt = target - nums[i] - nums[j]

                while left < right:
                    if nums[left] + nums[right] == tt:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1

                    elif nums[left] + nums[right] < tt:
                        left += 1
                    elif nums[left] + nums[right] > tt:
                        right -= 1
        return ans


# @lc code=end
