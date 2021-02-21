from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 0

        window = deque()
        ans = []
        while right < len(nums):
            while window and window[-1] < nums[right]:
                window.pop()

            window.append(nums[right])
            right += 1

            if right - left < k:
                continue
            elif right - left > k:
                if nums[left] == window[0]:
                    window.popleft()
                left += 1

            ans.append(window[0])

        return ans
