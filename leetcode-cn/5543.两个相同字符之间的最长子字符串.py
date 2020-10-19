#
# @lc app=leetcode.cn id=5543 lang=python3
#
# [5543] 两个相同字符之间的最长子字符串
#


# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mem = {}
        ans = -1

        for index, c in enumerate(s):
            if c not in mem:
                mem[c] = index
            else:
                ans = max(ans, index - mem[c] - 1)

        return ans


# @lc code=end
