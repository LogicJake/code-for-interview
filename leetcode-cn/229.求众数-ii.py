#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#

# @lc code=start
from typing import List

# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         times = {}
#         n = len(nums)
#         result = []
#         for num in nums:
#             if num not in times:
#                 times[num] = 1
#             else:
#                 times[num] += 1

#             if times[num] > n // 3 and num not in result:
#                 result.append(num)

#         return result


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums

        val1 = nums[0]
        count1 = 0

        val2 = nums[0]
        count2 = 0

        for num in nums:
            if num == val1:
                count1 += 1
                continue
            if num == val2:
                count2 += 1
                continue

            if count1 == 0:
                val1 = num
                count1 = 1
                continue
            if count2 == 0:
                val2 = num
                count2 = 1
                continue

            count2 -= 1
            count1 -= 1

        count1 = 0
        count2 = 0
        for num in nums:
            if num == val1:
                count1 += 1
            elif num == val2:
                count2 += 1

        result = []
        if count1 > len(nums) // 3:
            result.append(val1)
        if count2 > len(nums) // 3:
            result.append(val2)
        return result


# @lc code=end
