#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#

# @lc code=start
from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []

        start = 0

        for i in range(len(s)):
            if s[i] != s[start]:
                if i - start >= 3:
                    ans.append([start, i - 1])
                start = i

        if len(s) - start >= 3:
            ans.append([start, len(s) - 1])

        return ans


# @lc code=end
