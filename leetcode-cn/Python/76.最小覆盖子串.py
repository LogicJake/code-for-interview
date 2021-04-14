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

        ans = '0' * (len(s) + 1)

        cnt = {}
        window = {}
        num = 0

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
                    num += 1

            while num == len(cnt):
                if right - left < len(ans):
                    ans = s[left:right]

                c = s[left]
                left += 1

                if c in cnt:
                    if window[c] == cnt[c]:
                        num -= 1
                    window[c] -= 1

        return '' if len(ans) == len(s) + 1 else ans


# @lc code=end
