#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#


# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0

        while i < len(name) and j < len(typed):
            pre1 = name[i]
            cnt1 = 0

            while i < len(name) and name[i] == pre1:
                cnt1 += 1
                i += 1

            pre2 = typed[j]
            cnt2 = 0

            while j < len(typed) and typed[j] == pre2:
                cnt2 += 1
                j += 1

            if pre2 != pre1:
                return False

            if cnt2 < cnt1:
                return False

        if i != len(name) or j != len(typed):
            return False

        return True


# @lc code=end
