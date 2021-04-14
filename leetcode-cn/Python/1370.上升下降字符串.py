#
# @lc app=leetcode.cn id=1370 lang=python3
#
# [1370] 上升下降字符串
#


# @lc code=start
class Solution:
    def sortString(self, s: str) -> str:
        h = [0] * 26

        for c in s:
            h[ord(c) - 97] += 1

        def appendc(result, i):
            if h[i] > 0:
                result.append(chr(i + 97))
                h[i] -= 1

        result = []
        while 1:
            if len(result) == len(s):
                break

            for i in range(26):
                appendc(result, i)

            for i in range(26):
                appendc(result, 25 - i)

        return ''.join(result)


# @lc code=end
