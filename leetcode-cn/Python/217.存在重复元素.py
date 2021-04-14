#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mem = set()

        for num in nums:
            if num in mem:
                return True
            else:
                mem.add(num)

        return False


# @lc code=end
