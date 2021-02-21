class Solution:
    def strToInt(self, str: str) -> int:
        i = 0
        while i < len(str) and str[i] == ' ':
            i += 1

        if i == len(str):
            return 0

        flag = 1
        if str[i] == '+' or str[i] == '-':
            if str[i] == '-':
                flag = -1
            i += 1

        if i == len(str):
            return 0

        num = 0
        while i < len(str) and str[i] >= '0' and str[i] <= '9':
            num = num * 10 + int(str[i])
            i += 1

        num = flag * num

        if num > 2**31 - 1:
            num = 2**31 - 1

        if num < -2**31:
            num = -2**31
        return num
