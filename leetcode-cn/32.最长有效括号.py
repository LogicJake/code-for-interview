#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#


# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * (len(s))
        ans = 0

        for i, c in enumerate(s):
            if c == ')':
                if i - 1 >= 0:
                    if s[i - 1] == '(':
                        if i - 2 >= 0:
                            dp[i] = dp[i - 2] + 2
                        else:
                            dp[i] = 2
                    elif s[i - 1] == ')':
                        if i - 1 - dp[i - 1] >= 0 and s[i - 1 -
                                                        dp[i - 1]] == '(':
                            if i - 2 - dp[i - 1] >= 0:
                                dp[i] = dp[i - 1] + dp[i - 2 - dp[i - 1]] + 2
                            else:
                                dp[i] = dp[i - 1] + 2
                    ans = max(ans, dp[i])

        return ans


# @lc code=end
