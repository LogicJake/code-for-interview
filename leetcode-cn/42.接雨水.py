#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0

        for i in range(len(height)):
            while len(stack) != 0 and height[i] > height[stack[-1]]:
                cur = stack.pop()
                if len(stack) == 0:
                    break

                j = stack[-1]
                h = min(height[i], height[j]) - height[cur]
                w = i - j - 1
                ans += w * h

            stack.append(i)

        return ans


# @lc code=end
