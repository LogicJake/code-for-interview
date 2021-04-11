#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = 9999
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)

        ans = []
        i = 0

        while i < min_len:
            c = ''
            equal = True
            for s in strs:
                if c == '':
                    c = s[i]
                elif s[i] != c:
                    equal = False
                    break

            if not equal:
                break
            ans.append(c)
            i += 1

        return ''.join(ans)


# @lc code=end
