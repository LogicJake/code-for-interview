#
# @lc app=leetcode.cn id=319 lang=python3
#
# [319] 灯泡开关
#


# @lc code=start
class Solution:
    # def bulbSwitch(self, n: int) -> int:
    #     def help(status, i):
    #         for j in range(i - 1, n, i):
    #             status[j] = 1 - status[j]

    #     status = [0] * n
    #     for i in range(1, n + 1):
    #         help(status, i)

    #     return sum(status)

    def bulbSwitch(self, n: int) -> int:
        return int(n**0.5)


# @lc code=end
