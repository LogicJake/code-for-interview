#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        total_len = word_len * len(words)

        word_cnt = defaultdict(int)
        for word in words:
            word_cnt[word] += 1
        ans = []
        for i in range(len(s) - total_len + 1):
            subs = s[i:i + total_len]
            sub_word_cnt = defaultdict(int)

            wc = 0
            for j in range(0, total_len, word_len):
                word = subs[j:j + word_len]

                sub_word_cnt[word] += 1
                if sub_word_cnt[word] > word_cnt[word]:
                    break
                wc += 1

            if wc == len(words):
                ans.append(i)
        return ans


# @lc code=end
