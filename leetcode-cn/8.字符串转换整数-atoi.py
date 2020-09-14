#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#


# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        def is_num(c):
            if '0' <= c and c <= '9':
                return True
            return False

        i = 0
        while i < len(str) and str[i] == ' ':
            i += 1

        str = str[i:]

        if len(str) == 0 or (not is_num(str[0]) and str[0] != '-'
                             and str[0] != '+'):
            return 0

        flag = 1
        i = 0
        if str[0] == '-' or str[0] == '+':
            i += 1
            if str[0] == '-':
                flag = -1
        res = []
        while i < len(str) and is_num(str[i]):
            res.append(str[i])
            i += 1
        ans = 0
        for i, c in enumerate(res[::-1]):
            ans += int(c) * 10**(i)
        ans = ans * flag

        if ans < -2**31:
            ans = -2**31
        if ans > 2**31 - 1:
            ans = 2**31 - 1
        return ans


# @lc code=end
