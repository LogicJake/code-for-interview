#
# @lc app=leetcode.cn id=318 lang=python3
#
# [318] 最大单词长度乘积
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        hashmap = defaultdict(int)

        def bit_number(ch):
            return ord(ch) - ord('a')

        for word in words:
            bitmask = 0
            for ch in word:
                bitmask |= 1 << bit_number(ch)
            hashmap[bitmask] = max(hashmap[bitmask], len(word))

        max_len = 0
        for word1 in hashmap:
            for word2 in hashmap:
                if word1 & word2 == 0:
                    max_len = max(max_len, hashmap[word1] * hashmap[word2])

        return max_len


# @lc code=end
