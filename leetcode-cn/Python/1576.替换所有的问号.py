#
# @lc app=leetcode.cn id=1576 lang=python3
#
# [1576] 替换所有的问号
#

# @lc code=start
import string


class Solution:
    def modifyString(self, s: str) -> str:
        ns = list(s)

        for i, c in enumerate(s):
            if c == '?':
                print(c)
                for a in string.ascii_letters:
                    if (i - 1 < 0 or a != ns[i - 1]) and (i + 1 >= len(s)
                                                          or a != ns[i + 1]):
                        ns[i] = a
                        break

        return ''.join(ns)


# @lc code=end
