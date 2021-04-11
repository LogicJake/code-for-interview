#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        n = len(s)
        left, right = 0, 0
        for i in range(n):
            left1, right1 = expand(s, i, i)
            left2, right2 = expand(s, i, i + 1)

            if right1 - left1 > right - left:
                right, left = right1, left1

            if right2 - left2 > right - left:
                right, left = right2, left2

        return s[left:right + 1]


# @lc code=end
