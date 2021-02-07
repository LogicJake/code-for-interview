from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        i = 0

        while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
            i += 1

        if i == len(nums) - 1:
            return True

        i += 1

        while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
            i += 1

        if i == len(nums) - 1 and nums[i] <= nums[0]:
            return True
        else:
            return False
