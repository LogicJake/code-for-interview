class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        a = 1
        b = 1

        for i in range(2, len(s) + 1):
            tmp = s[i - 2:i]
            c = a + b if '10' <= tmp <= '25' else b
            a = b
            b = c

        return b
        