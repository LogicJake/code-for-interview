#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#

from functools import lru_cache
# @lc code=start
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def help(s):
            if s == '':
                return [[]]

            ans = []
            for i in range(len(s)):
                word = s[:i + 1]
                if word in wordDict:
                    next_ans = help(s[i + 1:])
                    for next in next_ans:
                        ans.append([word] + next[:])

            return ans

        ans = help(s)
        return [' '.join(words) for words in ans]


# @lc code=end
