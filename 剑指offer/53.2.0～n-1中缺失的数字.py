from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1

        return left
