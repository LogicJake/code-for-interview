#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        word_set = set(wordList)

        queue = [beginWord]
        visited = set()
        visited.add(beginWord)

        word_len = len(beginWord)
        num = 1
        while queue:
            sz = len(queue)
            for _ in range(sz):
                word = queue.pop(0)

                for i in range(word_len):
                    next_word = list(word)

                    for j in range(26):
                        next_word[i] = chr(ord('a') + j)
                        nw = ''.join(next_word)

                        if nw in word_set:
                            if nw == endWord:
                                return num + 1

                            if nw not in visited:
                                visited.add(nw)
                                queue.append(nw)

            num += 1

        return 0


# @lc code=end
