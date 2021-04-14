#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == ')':
                if stack and stack[-1] == '(':
                    stack.pop(-1)
                else:
                    return False
            elif c == ']':
                if stack and stack[-1] == '[':
                    stack.pop(-1)
                else:
                    return False
            elif c == '}':
                if stack and stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False


# @lc code=end
