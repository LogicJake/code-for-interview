from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def help(target):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        return help(target) - help(target - 1)
