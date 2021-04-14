#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 找到一个0，然后再往后找出非0元素交换
        for i, num in enumerate(nums):
            if num != 0:
                continue

            j = i + 1
            while j < len(nums):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                j += 1

            if j == len(nums):
                break


# @lc code=end
