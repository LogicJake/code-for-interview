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
            while stack and height[stack[-1]] < height[i]:
                top = stack[-1]
                stack.pop(-1)

                if not stack:
                    continue

                distance = i - stack[-1] - 1
                h = min(height[i], height[stack[-1]]) - height[top]

                ans += h * distance

            stack.append(i)

        return ans


# @lc code=end
