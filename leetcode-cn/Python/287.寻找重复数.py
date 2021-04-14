#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
from typing import List


class Solution:
    # def findDuplicate(self, nums: List[int]) -> int:
    #     exist = set()

    #     for num in nums:
    #         if num in exist:
    #             return num
    #         else:
    #             exist.add(num)
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        pre = 0

        while pre != slow:
            pre = nums[pre]
            slow = nums[slow]

        return pre


# @lc code=end
