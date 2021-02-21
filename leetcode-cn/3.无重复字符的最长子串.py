#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        mem = defaultdict(int)
        ans = 0

        while right < len(s):
            c = s[right]
            mem[c] += 1
            right += 1

            while mem[c] > 1:
                mem[s[left]] -= 1
                left += 1

            ans = max(ans, right - left)

        return ans


# @lc code=end
