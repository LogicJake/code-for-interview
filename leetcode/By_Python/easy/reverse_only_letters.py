# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-10-31 17:33:45
# @Last Modified time: 2018-10-31 19:03:46


class Solution(object):

    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """

        s = []

        for index in range(len(S) - 1, -1, -1):
            if S[index].isalpha():
                s.append(S[index])

        for index, c in enumerate(S):
            if not c.isalpha():
                s.insert(index, c)

        return ''.join(s)

if __name__ == '__main__':
    solution = Solution()

    s = "Test1ng-Leet=code-Q!"
    solution.reverseOnlyLetters(s)
