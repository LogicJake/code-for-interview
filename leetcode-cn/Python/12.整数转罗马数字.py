#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#


# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []

        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        value_char = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        while num != 0:
            for value in values:
                if value <= num:
                    ans.append(value_char[value])
                    num -= value
                    break

        return ''.join(ans)


# @lc code=end
