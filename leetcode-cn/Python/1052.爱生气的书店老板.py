#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int],
                     X: int) -> int:
        left = 0
        right = 0

        window = 0
        increase = 0
        while right < len(customers):
            if grumpy[right] == 1:
                window += customers[right]
            right += 1

            if right - left < X:
                continue
            elif right - left > X:
                if grumpy[left] == 1:
                    window -= customers[left]
                left += 1

            increase = max(increase, window)

        ans = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                ans += customers[i]

        return ans + increase


# @lc code=end
