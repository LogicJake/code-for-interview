#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pattern_map = {}
        str_map = {}

        if len(str.split(' ')) != len(pattern):
            return False

        for i, s in enumerate(str.split(' ')):
            if i >= len(pattern):
                return False
            p = pattern[i]

            if (p in pattern_map
                    and pattern_map[p] != s) or (s in str_map
                                                 and str_map[s] != p):
                return False
            if p not in pattern_map:
                pattern_map[p] = s
            if s not in str_map:
                str_map[s] = p

        return True


# @lc code=end
