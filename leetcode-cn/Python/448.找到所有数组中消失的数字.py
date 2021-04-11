#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for num in nums:
            x = (num - 1) % n
            nums[x] += n

        ans = []
        for index, num in enumerate(nums):
            if num <= n:
                ans.append(index + 1)
        return ans


# @lc code=end
