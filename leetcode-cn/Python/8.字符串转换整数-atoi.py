#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#


# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        res = 0
        i = 0
        n = len(str)
        flag = True

        while i < n and str[i] == ' ':
            i += 1

        if i < n and str[i] == '-':
            flag = False
        if i < n and (str[i] == '+' or str[i] == '-'):
            i += 1

        while i < n and str[i].isdigit():
            num = int(str[i])
            res = res * 10 + num

            i += 1

        if not flag:
            res = -res

        if res > 2**31 - 1:
            res = 2**31 - 1
        if res < -2**31:
            res = -2**31

        return res


# @lc code=end
