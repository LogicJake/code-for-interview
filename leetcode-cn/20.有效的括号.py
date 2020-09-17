#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) % 2 == 1:
        #     return False
        stack = []

        pairs = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != pairs[c]:
                    return False
                else:
                    stack.pop()

        return not stack


# @lc code=end
