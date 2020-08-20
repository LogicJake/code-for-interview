#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
from typing import List

from collections import defaultdict

# class Solution:
#     def singleNumber(self, nums: List[int]) -> List[int]:
#         count = defaultdict(int)

#         for num in nums:
#             count[num] += 1

#         result = []
#         for k in count:
#             if count[k] == 1:
#                 result.append(k)

#         return result


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for num in nums:
            diff = diff ^ num

        diff = diff & -diff

        result = [0, 0]
        for num in nums:
            if diff & num == 0:
                result[0] ^= num
            else:
                result[1] ^= num

        return result


# @lc code=end
