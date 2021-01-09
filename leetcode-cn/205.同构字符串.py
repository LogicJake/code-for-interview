#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#


# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mem1 = {}
        mem2 = {}

        if len(s) != len(t):
            return False

        for i, cs in enumerate(s):
            ct = t[i]

            if cs in mem1 and mem1[cs] != ct or (ct in mem2
                                                 and mem2[ct] != cs):
                return False
            else:
                mem1[cs] = ct
                mem2[ct] = cs
        return True


# @lc code=end
