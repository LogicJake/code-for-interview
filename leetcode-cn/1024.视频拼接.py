#
# @lc app=leetcode.cn id=1024 lang=python3
#
# [1024] 视频拼接
#

# @lc code=start
from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [float('inf')] * (T + 1)
        dp[0] = 0

        for t in range(1, T + 1):
            for start, end in clips:
                if start < t <= end:
                    dp[t] = min(dp[t], dp[start] + 1)

        return -1 if dp[-1] == float('inf') else dp[-1]


# @lc code=end
