#
# @lc app=leetcode.cn id=649 lang=python3
#
# [649] Dota2 参议院
#

# @lc code=start


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        radiant = []
        dire = []

        for i, c in enumerate(senate):
            if c == 'D':
                dire.append(i)
            else:
                radiant.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)

            radiant.pop(0)
            dire.pop(0)

        return 'Radiant' if radiant else 'Dire'


# @lc code=end
