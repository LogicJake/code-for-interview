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
            while stack and height[stack[-1]] < h:
                button_index = stack.pop(-1)

                if not stack:
                    break

                width = i - stack[-1] - 1

                hh = min(h, height[stack[-1]]) - height[button_index]

                ans += hh * width

            stack.append(i)

        return ans


# @lc code=end
