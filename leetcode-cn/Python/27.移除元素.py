#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0

        for i in range(len(nums)):
            if i == len(nums) - 1 and (nums[i] != val and nums[i] != -1):
                return i + 1

            if nums[i] == val or nums[i] == -1:
                if j <= i:
                    j = i + 1

                while j < len(nums) and nums[j] == val:
                    j += 1

                if j == len(nums):
                    break

                nums[i] = nums[j]
                nums[j] = -1

                j += 1
        return i


# @lc code=end
