#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value_index = {}

        for i, num in enumerate(nums):
            if num not in value_index:
                value_index[num] = i
            else:
                if abs(value_index[num] - i) <= k:
                    return True
                else:
                    value_index[num] = i
        return False


# @lc code=end
