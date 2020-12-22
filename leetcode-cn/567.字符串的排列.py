#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#


# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        valid = 0
        left = 0
        right = 0
        cnt = {}
        window = {}

        for c in s1:
            if c not in cnt:
                cnt[c] = 1
            else:
                cnt[c] += 1

            window[c] = 0

        while right < len(s2):
            c = s2[right]
            right += 1

            if c in cnt:
                window[c] += 1
                if window[c] == cnt[c]:
                    valid += 1

            if right - left == len(s1):
                if valid == len(cnt):
                    return True

                c = s2[left]
                left += 1

                if c in cnt:
                    if window[c] == cnt[c]:
                        valid -= 1
                    window[c] -= 1

        return False


# @lc code=end
