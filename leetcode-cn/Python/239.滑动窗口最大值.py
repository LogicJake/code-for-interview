#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
from typing import List
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 0
        window = []

        n = len(nums)
        ans = []
        while right < n:
            heapq.heappush(window, (-nums[right], right))
            right += 1

            if right - left >= k:
                while window[0][1] < left:
                    heapq.heappop(window)
                ans.append(-window[0][0])
                left += 1

        return ans


# @lc code=end
