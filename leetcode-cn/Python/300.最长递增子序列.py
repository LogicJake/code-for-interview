#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def first_large(nums, target):
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1

            return left

        ans = []
        for num in nums:
            if not ans or num > ans[-1]:
                ans.append(num)
            else:
                loc = first_large(ans, num)
                ans[loc] = num

        return len(ans)


# @lc code=end
