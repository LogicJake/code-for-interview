#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#


# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        # aeiou
        tool = 'aeiouAEIOU'
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            while s[i] not in tool and i < j:
                i += 1

            while s[j] not in tool and i < j:
                j -= 1

            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return ''.join(s)


# @lc code=end
