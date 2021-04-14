#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        for i, c in enumerate(s):
            if cnt[ord(c) - ord('a')] == 1:
                return i

        return -1


# @lc code=end
