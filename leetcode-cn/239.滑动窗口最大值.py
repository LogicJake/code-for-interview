#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        n = len(nums)

        if n == 0 or k == 0:
            return []

        if n == 1:
            return nums

        def clean(i):
            if q and q[0] == i - k:
                q.popleft()

            while q and nums[i] > nums[q[-1]]:
                q.pop()

            q.append(i)

        max_id = 0
        for i in range(k):
            clean(i)
            if nums[i] > nums[max_id]:
                max_id = i
        output = [nums[max_id]]

        for i in range(k, n):
            clean(i)
            output.append(nums[q[0]])

        return output


# @lc code=end
