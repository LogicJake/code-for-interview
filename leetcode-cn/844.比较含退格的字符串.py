#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#


# @lc code=start
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1 = []
        stack2 = []

        for c in S:
            if c != '#':
                stack1.append(c)
            elif len(stack1) != 0:
                stack1.pop()

        for c in T:
            if c != '#':
                stack2.append(c)
            elif len(stack2) != 0:
                stack2.pop()

        if len(stack1) != len(stack2):
            return False

        i = 0
        j = 0

        while i != len(stack1):
            if stack1[i] != stack2[j]:
                return False

            i += 1
            j += 1

        return True


# @lc code=end
