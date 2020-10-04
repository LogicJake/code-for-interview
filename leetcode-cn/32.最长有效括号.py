#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#


# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        ans = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    if i - 2 >= 0:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                else:
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                        if i - dp[i - 1] - 2 >= 0:
                            dp[i] = dp[i - dp[i - 1] - 2] + dp[i - 1] + 2
                        else:
                            dp[i] = dp[i - 1] + 2

                ans = max(ans, dp[i])
        return ans


# @lc code=end
