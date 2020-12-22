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
        window = defaultdict(int)
        ans = 0

        while right < len(s):
            c = s[right]
            right += 1

            window[c] += 1

            while window[c] > 1:
                d = s[left]
                left += 1

                window[d] -= 1

            ans = max(ans, right - left)

        return ans


# @lc code=end
