#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#


# @lc code=start
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []

        for c in S:
            if stack and stack[-1] == c:
                stack.pop(-1)
            else:
                stack.append(c)

        return ''.join(stack)


# @lc code=end
