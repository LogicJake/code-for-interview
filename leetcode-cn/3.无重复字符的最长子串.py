#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        right = -1
        visited = set()
        for left in range(len(s)):
            if left != 0:
                visited.remove(s[left - 1])

            while right + 1 < len(s) and s[right + 1] not in visited:
                right += 1
                visited.add(s[right])

            result = max(result, right - left + 1)

        return result


# @lc code=end
