#
# @lc app=leetcode.cn id=398 lang=python3
#
# [398] 随机数索引
#

# @lc code=start
from typing import List
import random


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        nums = self.nums

        cnt = 0
        ans = 0

        for i, num in enumerate(nums):
            if num == target:
                cnt += 1

                if random.randint(0, cnt - 1) == 0:
                    ans = i

        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end
