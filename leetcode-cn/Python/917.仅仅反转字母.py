#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#


# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        chars = []
        others = {}

        for i, c in enumerate(S):
            if c.isalpha():
                chars.append(c)
            else:
                others[i] = c

        ans = [''] * (len(chars) + len(others))
        for i in range(len(ans)):
            if i in others:
                ans[i] = others[i]
            else:
                ans[i] = chars.pop()

        return ''.join(ans)


# @lc code=end
