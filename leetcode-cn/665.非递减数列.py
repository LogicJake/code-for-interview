#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                cnt += 1

                if cnt > 1:
                    return False
                if i > 0 and nums[i + 1] < nums[i - 1]:
                    nums[i + 1] = nums[i]

        return True


# @lc code=end
