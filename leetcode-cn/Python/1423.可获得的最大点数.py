#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
#

# @lc code=start
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        k = len(cardPoints) - k
        left = 0
        right = 0
        total = sum(cardPoints)
        ans = 999999999999
        tmp = 0

        while right < len(cardPoints):
            tmp += cardPoints[right]
            right += 1

            while right - left > k:
                tmp -= cardPoints[left]
                left += 1

            if right - left == k:
                ans = min(ans, tmp)

        return total - ans


# @lc code=end
