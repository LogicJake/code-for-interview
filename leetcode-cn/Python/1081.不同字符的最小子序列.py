#
# @lc app=leetcode.cn id=1081 lang=python3
#
# [1081] 不同字符的最小子序列
#


# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []

        last_seen = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c not in stack:
                while stack and c < stack[-1] and last_seen[stack[-1]] > i:
                    stack.pop()

                stack.append(c)

        return ''.join(stack)


# @lc code=end
