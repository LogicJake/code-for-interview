from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> str:
        cnt = defaultdict(int)

        for c in s:
            cnt[c] += 1

        for c in s:
            if cnt[c] == 1:
                return c

        return ' '
