#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#


# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        flag = 0
        nums = []

        while i >= 0 or j >= 0 or flag:
            tmp = 0
            if i >= 0:
                tmp += ord(num1[i]) - ord('0')
            if j >= 0:
                tmp += ord(num2[j]) - ord('0')

            tmp += flag
            flag = tmp // 10
            tmp = tmp % 10

            nums.append(str(tmp))

            i -= 1
            j -= 1

        return ''.join(nums[::-1])


# @lc code=end
