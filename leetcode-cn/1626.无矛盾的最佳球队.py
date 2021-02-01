#
# @lc app=leetcode.cn id=1626 lang=python3
#
# [1626] 无矛盾的最佳球队
#

# @lc code=start
from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)

        arr = sorted(zip(ages, scores))

        dp = [arr[i][1] for i in range(n)]

        for i in range(n):
            for j in range(i):
                if arr[j][1] <= arr[i][1]:
                    dp[i] = max(dp[i], dp[j] + arr[i][1])

        return max(dp)


# @lc code=end
