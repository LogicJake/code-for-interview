#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
from typing import List


class Solution:
    '''
    暴力 O(n*n)，超时
    def maxArea(self, height: List[int]) -> int:
        cap = 0
        for i, h1 in enumerate(height):
            for j, h2 in enumerate(height):
                width = j - i
                h = h1 if h1 < h2 else h2
                if width * h > cap:
                    cap = width * h
        return cap
    '''
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_cap = 0

        while (i < j):
            h = height[i] if height[i] < height[j] else height[j]
            cap = (j - i) * h

            if cap > max_cap:
                max_cap = cap

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return max_cap


# @lc code=end
