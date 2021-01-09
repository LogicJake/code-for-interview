#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#


# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0

        for c in s:
            ans = ans ^ ord(c)

        for c in t:
            ans = ans ^ ord(c)

        return chr(ans)


# @lc code=end
