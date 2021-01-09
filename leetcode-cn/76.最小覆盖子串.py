#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#


# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        valid = 0

        cnt = {}
        window = {}
        start = 0
        length = float('inf')

        for c in t:
            if c in cnt:
                cnt[c] += 1
            else:
                cnt[c] = 1
            window[c] = 0

        while right < len(s):
            c = s[right]
            right += 1

            if c in cnt:
                window[c] += 1
                if window[c] == cnt[c]:
                    valid += 1

            while valid == len(cnt):
                if right - left < length:
                    start = left
                    length = right - left

                c = s[left]
                left += 1

                if c in cnt:
                    if window[c] == cnt[c]:
                        valid -= 1
                    window[c] -= 1

        return '' if length == float('inf') else s[start:start + length]


# @lc code=end
