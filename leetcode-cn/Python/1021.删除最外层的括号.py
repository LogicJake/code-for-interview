#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#


# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []

        ans = ''

        for c in S:
            if c == '(':
                if stack:
                    ans += c
                stack.append(c)
            else:
                stack.pop(-1)
                if stack:
                    ans += c

        return ans


# @lc code=end
