#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#


# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        list_n = list(str(N))
        r = len(list_n) - 1
        res = []
        while r - 1 >= 0:
            if list_n[r] >= list_n[r - 1]:
                res.append(list_n[r])
            else:
                list_n[r - 1] = str(int(list_n[r - 1]) - 1)
                res = ['9'] * (len(res) + 1)
            r -= 1
        if list_n[r] != '0':
            res.append(list_n[r])
        return int(''.join(res[::-1]))


# @lc code=end
