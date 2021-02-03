#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#


# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        cnt = 0
        left = 0

        ans = []
        for i, c in enumerate(S):
            if c == '(':
                cnt += 1
            else:
                cnt -= 1

            if cnt == 0:
                ans.append(S[left + 1:i])
                left = i + 1
        return ''.join(ans)


# @lc code=end
