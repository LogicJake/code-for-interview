#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#


# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        ans = 0
        for c in s:
            if c != ' ':
                cnt += 1
            else:
                if cnt != 0:
                    ans = cnt
                cnt = 0
        if cnt != 0:
            ans = cnt
        return ans


# @lc code=end
