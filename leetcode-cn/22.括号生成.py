#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List


class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:
    #     if n == 0:
    #         return ['']

    #     ans = []
    #     for left in range(n):
    #         right = n - left - 1
    #         a_list = self.generateParenthesis(left)
    #         b_list = self.generateParenthesis(right)
    #         for a in a_list:
    #             for b in b_list:
    #                 ans.append('({}){}'.format(a, b))

    #     return ans

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def help(s, left, right):
            if len(s) == 2 * n:
                ans.append(''.join(s))
                return

            if left < n:
                s.append('(')
                help(s, left + 1, right)
                s.pop()

            if right < left:
                s.append(')')
                help(s, left, right + 1)
                s.pop()

        help([], 0, 0)
        return ans


# @lc code=end
