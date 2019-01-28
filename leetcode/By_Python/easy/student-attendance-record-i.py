# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-28 16:55:20
# @Last Modified time: 2019-01-28 17:03:38


class Solution:

    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_num = 0
        l_num = 0
        for r in s:
            if r == 'A':
                a_num += 1
                l_num = 0
            elif r == 'L':
                l_num += 1
                if l_num > 2:
                    return False
            else:
                l_num = 0

            if a_num > 2 or a_num > 1:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    s = "LALL"
    res = solution.checkRecord(s)
    print(res)
