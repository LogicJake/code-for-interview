#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        left = 0
        right = 0
        valid = 0
        cnt = {}
        window = {}

        for c in p:
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

            if right - left == len(p):
                if valid == len(cnt):
                    ans.append(left)

                c = s[left]
                left += 1

                if c in cnt:
                    if window[c] == cnt[c]:
                        valid -= 1

                    window[c] -= 1

        return ans


# @lc code=end
