# -*- coding: utf-8 -*-
# @Time    : 18-10-20 下午12:04
# @Author  : LogicJake
# @File    : to_lower_case.py


class Solution:

    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = [chr(ord(c) + 32) if c >= 'A' and c <= 'Z' else c for c in str]
        return ''.join(res)


if __name__ == '__main__':
    solution = Solution()
    solution.toLowerCase('Hello')
