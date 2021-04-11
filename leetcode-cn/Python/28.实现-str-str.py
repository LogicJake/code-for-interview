#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#


# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        for i, c in enumerate(haystack):
            if c == needle[0] and haystack[i:i + len(needle)] == needle:
                return i

        return -1


# @lc code=end
