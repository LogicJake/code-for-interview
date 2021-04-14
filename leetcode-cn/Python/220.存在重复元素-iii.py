#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#

# @lc code=start
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int,
                                      t: int) -> bool:
        # 错误情况，绝对值肯定大于等于0
        if k < 0 or t < 0:
            return False

        bucket_size = t + 1
        buckets = {}

        for i, num in enumerate(nums):
            bucket_id = num // bucket_size

            if bucket_id in buckets:
                return True
            if bucket_id - 1 in buckets and num - buckets[bucket_id - 1] <= t:
                return True

            if bucket_id + 1 in buckets and buckets[bucket_id + 1] - num <= t:
                return True

            buckets[bucket_id] = num

            if i >= k:
                buckets.pop(nums[i - k] // bucket_size)

        return False


# @lc code=end
