#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#


# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        s = self.countAndSay(n - 1)

        i = 0
        res = ''

        for j, c in enumerate(s):
            if c != s[i]:
                res += str(j - i) + s[i]
                i = j

        res += str(len(s) - i) + s[-1]
        return res


# @lc code=end
