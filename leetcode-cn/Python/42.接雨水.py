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

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                index = stack.pop(-1)

                if not stack:
                    break

                ans += (min(h, height[stack[-1]]) -
                        height[index]) * (i - stack[-1] - 1)

            stack.append(i)

        return ans


# @lc code=end
