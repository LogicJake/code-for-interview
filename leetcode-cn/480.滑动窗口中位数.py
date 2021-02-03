#
# @lc app=leetcode.cn id=480 lang=python3
#
# [480] 滑动窗口中位数
#

import bisect
# @lc code=start
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)

        start = 0

        window = sorted(nums[:k])
        res = [window[k // 2]
               ] if k % 2 else [(window[k // 2] + window[k // 2 - 1]) / 2]

        for i in range(k, n):
            bisect.insort(window, nums[i])
            window.pop(bisect.bisect_left(window, nums[start]))
            start += 1

            if k % 2 == 1:
                res.append(window[k // 2])
            else:
                res.append((window[k // 2] + window[k // 2 - 1]) / 2)

        return res


# @lc code=end
