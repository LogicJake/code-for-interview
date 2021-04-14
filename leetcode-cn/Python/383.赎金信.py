#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = defaultdict(int)
        for c in magazine:
            cnt[c] += 1

        for c in ransomNote:
            if cnt[c] < 1:
                return False
            cnt[c] -= 1

        return True


# @lc code=end
