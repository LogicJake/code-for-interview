#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#

# @lc code=start


class Solution:
    def calculate(self, s: str) -> int:
        v = 0
        sign = 1
        res = 0
        stack = []
        for c in s:
            if c.isdigit():
                v = v * 10 + int(c)

            if c == '+':
                res += sign * v
                v = 0
                sign = 1

            if c == '-':
                res += sign * v
                v = 0
                sign = -1

            if c == '(':
                stack.append(res)
                stack.append(sign)

                v = 0
                sign = 1
                res = 0

            if c == ')':
                res += sign * v
                res *= stack.pop()
                res += stack.pop()

                v = 0

        return res + sign * v


# @lc code=end
