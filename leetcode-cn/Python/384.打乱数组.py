#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#

# @lc code=start
from typing import List
import random


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = list(nums)
        self.origin = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = list(self.origin)
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = self.nums
        for i in range(len(nums)):
            swap = random.randrange(i, len(nums))
            nums[swap], nums[i] = nums[i], nums[swap]

        return nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end
