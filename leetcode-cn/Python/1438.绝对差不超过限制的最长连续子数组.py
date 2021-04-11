#
# @lc app=leetcode.cn id=1438 lang=python3
#
# [1438] 绝对差不超过限制的最长连续子数组
#

# @lc code=start
from typing import List

from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        right = 0
        ans = 0

        max_que = deque()
        min_que = deque()

        while right < len(nums):
            while max_que and max_que[-1] < nums[right]:
                max_que.pop()
            while min_que and min_que[-1] > nums[right]:
                min_que.pop()

            max_que.append(nums[right])
            min_que.append(nums[right])

            right += 1

            while max_que[0] - min_que[0] > limit:
                if max_que[0] == nums[left]:
                    max_que.popleft()
                if min_que[0] == nums[left]:
                    min_que.popleft()

                left += 1

            ans = max(ans, right - left)

        return ans


# @lc code=end
