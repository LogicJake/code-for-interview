from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0

        window = defaultdict(int)

        while right < len(s):
            window[s[right]] += 1
            right += 1

            while left < right and window[s[right - 1]] == 2:
                window[s[left]] -= 1
                left += 1

            ans = max(ans, right - left)

        return ans
