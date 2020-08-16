#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#

# @lc code=start


class Solution:
    def evaluate(self, stack):
        if len(stack) != 0:
            res = stack.pop()
        else:
            res = 0

        while len(stack) != 0 and stack[-1] != ')':
            op = stack.pop()
            if op == '+':
                res += stack.pop()
            else:
                res -= stack.pop()

        return res

    def calculate(self, s: str) -> int:
        stack = []
        n = 0
        v = 0

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if ch.isdigit():
                v += (10**n * int(ch))
                n += 1
            elif ch != ' ':
                if n > 0:
                    stack.append(v)
                    n = 0
                    v = 0

                if ch != '(':
                    stack.append(ch)
                else:
                    res = self.evaluate(stack)
                    stack.pop()
                    stack.append(res)

        if n > 0:
            stack.append(v)

        return self.evaluate(stack)


# @lc code=end
