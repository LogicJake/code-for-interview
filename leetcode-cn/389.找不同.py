#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt = defaultdict(int)

        for c in s:
            cnt[c] += 1

        for c in t:
            cnt[c] -= 1

            if cnt[c] < 0:
                return c


# @lc code=end
