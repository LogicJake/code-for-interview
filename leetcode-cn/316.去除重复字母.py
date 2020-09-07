#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#


# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []

        last_seen = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c not in stack:
                while stack and c < stack[-1] and last_seen[stack[-1]] > i:
                    stack.pop()

                stack.append(c)

        return ''.join(stack)


# @lc code=end
