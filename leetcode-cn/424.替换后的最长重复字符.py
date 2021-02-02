#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#

# @lc code=start
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        cnt = defaultdict(int)
        ans = 0

        def getMaxFreq(cnt):
            maxn = 0

            for v in cnt.values():
                maxn = max(maxn, v)

            return maxn

        while right < len(s):
            cnt[s[right]] += 1
            right += 1

            maxn = getMaxFreq(cnt)
            while right - left > maxn + k:
                cnt[s[left]] -= 1
                left += 1
                maxn = getMaxFreq(cnt)

            ans = max(ans, right - left)

        return ans


# @lc code=end
