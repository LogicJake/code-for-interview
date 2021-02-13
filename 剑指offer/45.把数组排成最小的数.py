from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def quick_sort(nums, left, right):
            if left >= right:
                return

            i = left
            j = right

            privot = nums[left]

            while i < j:
                while i < j and nums[j] + privot > privot + nums[j]:
                    j -= 1
                nums[i] = nums[j]

                while i < j and nums[i] + privot <= privot + nums[i]:
                    i += 1
                nums[j] = nums[i]

            nums[i] = privot

            quick_sort(nums, left, i - 1)
            quick_sort(nums, i + 1, right)

        nums = [str(num) for num in nums]
        quick_sort(nums, 0, len(nums) - 1)
        return ''.join(nums)
