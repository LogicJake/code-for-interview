# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-28 17:04:24
# @Last Modified time: 2019-01-28 17:23:38


class Solution:

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i = 0
        res = []
        while i < len(s):
            temp = s[i:i + k]
            res.append(temp[::-1])
            res.append(s[i + k:i + 2 * k])
            i += 2 * k

        return ''.join(res)


if __name__ == '__main__':
    solution = Solution()
    s = "abcdefg"
    k = 2
    res = solution.reverseStr(s, k)
    print(res)
