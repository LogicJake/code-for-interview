#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        res = ''
        for ll in range(n):
            for i in range(n):
                j = i + ll
                if j >= n:
                    break

                if ll == 0:
                    dp[i][j] = True
                elif ll == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])

                if dp[i][j] and ll + 1 > len(res):
                    res = s[i:j + 1]

        return res


# @lc code=end
