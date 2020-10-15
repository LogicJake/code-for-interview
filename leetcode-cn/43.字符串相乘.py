#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#


# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = []
        for i, c1 in enumerate(num2[::-1]):
            for j, c2 in enumerate(num1[::-1]):
                n1 = int(c1)
                n2 = int(c2)

                ans = n1 * n2
                index = j + i

                if index == len(res):
                    res.append(ans)
                else:
                    res[index] += ans

        flag = 0
        ans = []
        for num in res:
            num = num + flag
            flag = num // 10
            num = num % 10
            ans.append(str(num))

        if flag != 0:
            ans.append(str(flag))

        ans = ans[::-1]
        while len(ans) > 1 and ans[0] == '0':
            ans.pop(0)

        return ''.join(ans)


# @lc code=end
