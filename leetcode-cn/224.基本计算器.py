#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#

# @lc code=start


class Solution:
    def calculate(self, s: str) -> int:
        def help(stack):
            # stack[-1] != ') 考虑到有空括号
            if len(stack) != 0 and stack[-1] != ')':
                res = stack.pop()
            else:
                res = 0

            while stack and stack[-1] != ')':
                op = stack.pop()
                if op == '+':
                    res += stack.pop()
                else:
                    res -= stack.pop()

            return res

        s = list(s)
        s = s[::-1]

        n = 0
        v = 0
        stack = []
        for c in s:
            if c.isdigit():
                v += int(c) * 10**n
                n += 1
            else:
                if n > 0:
                    stack.append(v)
                    v = 0
                    n = 0

                if c == ' ':
                    continue

                if c != '(':
                    stack.append(c)
                else:
                    res = help(stack)
                    stack.pop()
                    stack.append(res)

        if n > 0:
            stack.append(v)

        return help(stack)


# @lc code=end
