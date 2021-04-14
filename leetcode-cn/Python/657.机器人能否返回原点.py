#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        U_cnt = 0
        R_cnt = 0

        for m in moves:
            if m == 'U':
                U_cnt += 1
                continue
            if m == 'D':
                U_cnt -= 1
                continue
            if m == 'L':
                R_cnt -= 1
                continue
            if m == 'R':
                R_cnt += 1
                continue

        if U_cnt == 0 and R_cnt == 0:
            return True
        else:
            return False


# @lc code=end
