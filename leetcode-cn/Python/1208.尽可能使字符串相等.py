#
# @lc app=leetcode.cn id=1208 lang=python3
#
# [1208] 尽可能使字符串相等
#


# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        right = 0
        n = len(s)

        sum_ = 0
        ans = 0
        while right < n:
            sum_ += abs(ord(s[right]) - ord(t[right]))
            right += 1

            while sum_ > maxCost:
                sum_ -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            ans = max(ans, right - left)

        return ans


# @lc code=end
