#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#


# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j = set()
        for c in J:
            j.add(c)

        ans = 0

        for c in S:
            if c in j:
                ans += 1

        return ans


# @lc code=end
