from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        cur = 0

        ans = 0

        for num in nums:
            cur = num + max(pre, 0)
            ans = max(ans, cur)
            pre = cur

        return ans
