#
# @lc app=leetcode.cn id=164 lang=python3
#
# [164] 最大间距
#

# @lc code=start
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        def radix_sort(nums):
            max_num = max(nums)
            max_num_len = len(str(max_num))
            i = 0
            while i < max_num_len:
                bucket_list = [[] for _ in range(10)]
                for num in nums:
                    bucket_list[int(num / 10**i) % 10].append(num)
                nums.clear()
                for num_list in bucket_list:
                    for num in num_list:
                        nums.append(num)
                i += 1

        if len(nums) < 2:
            return 0

        radix_sort(nums)

        max_gap = 0
        for i in range(len(nums) - 1):
            max_gap = max(max_gap, nums[i + 1] - nums[i])

        return max_gap


# @lc code=end
