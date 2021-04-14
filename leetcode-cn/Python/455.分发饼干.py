#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        j = 0
        ans = 0

        for num in g:
            while j < len(s) and s[j] < num:
                j += 1

            if j == len(s):
                break
            else:
                ans += 1
                j += 1

        return ans


# @lc code=end
