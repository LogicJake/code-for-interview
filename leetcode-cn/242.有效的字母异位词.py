#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
from collections import defaultdict


class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False

    #     s = list(s)
    #     t = list(t)

    #     s.sort()
    #     t.sort()

    #     for i in range(len(s)):
    #         if s[i] != t[i]:
    #             return False

    #     return True

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = defaultdict(int)

        for i in range(len(s)):
            count[s[i]] += 1
            count[t[i]] -= 1

        for k in count.keys():
            if count[k] != 0:
                return False

        return True


# @lc code=end
