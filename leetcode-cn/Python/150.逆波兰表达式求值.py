#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                num1 = stack.pop(-1)
                num2 = stack.pop(-1)

                res = num1 + num2
                stack.append(res)
            elif token == '-':
                num1 = stack.pop(-1)
                num2 = stack.pop(-1)

                res = num2 - num1
                stack.append(res)
            elif token == '*':
                num1 = stack.pop(-1)
                num2 = stack.pop(-1)

                res = num1 * num2
                stack.append(res)
            elif token == '/':
                num1 = stack.pop(-1)
                num2 = stack.pop(-1)

                res = int(num2 / float(num1))
                stack.append(res)
            else:
                stack.append(int(token))

        return stack[-1]


# @lc code=end
