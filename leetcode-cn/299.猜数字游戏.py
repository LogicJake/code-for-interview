#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#

# @lc code=start
from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cnt = defaultdict(int)
        index_map = defaultdict(list)

        for i, s in enumerate(secret):
            index_map[s].append(i)
            cnt[s] += 1

        a = 0
        b = 0
        for i, s in enumerate(guess):
            if s in index_map:
                if i in index_map[s]:
                    cnt[s] -= 1
                    a += 1

        for i, s in enumerate(guess):
            if s in index_map and i not in index_map[s] and cnt[s] != 0:
                cnt[s] -= 1
                b += 1

        return str(a) + 'A' + str(b) + 'B'


# @lc code=end
