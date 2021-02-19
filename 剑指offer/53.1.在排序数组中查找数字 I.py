from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def help(target):
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1

            return left

        return help(target) - help(target - 1)
