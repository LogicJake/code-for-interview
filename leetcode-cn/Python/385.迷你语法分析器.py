#
# @lc app=leetcode.cn id=385 lang=python3
#
# [385] 迷你语法分析器
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#     def __init__(self, value=None):
#         """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#     def isInteger(self):
#         """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#     def add(self, elem):
#         """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#     def setInteger(self, value):
#         """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#     def getInteger(self):
#         """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#     def getList(self):
#         """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))

        num = 0
        sign = 1
        is_num = False
        stack = []

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
                is_num = True

            elif c == '-':
                sign = -1
            elif c == '[':
                stack.append(NestedInteger())
            elif c == ']' or c == ',':
                if is_num:
                    last_nes = stack.pop()
                    last_nes.add(NestedInteger(num * sign))
                    stack.append(last_nes)

                num = 0
                sign = 1
                is_num = False

                if c == ']' and len(stack) > 1:
                    last_nes = stack.pop()
                    stack[-1].add(last_nes)

        return stack[0]


# @lc code=end
