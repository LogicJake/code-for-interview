#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#


# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]

        i = 0
        carry = 0
        ans = []
        while i < len(a) or i < len(b) or carry:
            if i < len(a):
                n1 = int(a[i])
            else:
                n1 = 0

            if i < len(b):
                n2 = int(b[i])
            else:
                n2 = 0

            res = (n1 + n2 + carry) % 2
            carry = (n1 + n2 + carry) // 2
            ans.append(str(res))
            i += 1

        return ''.join(ans[::-1])


# @lc code=end
