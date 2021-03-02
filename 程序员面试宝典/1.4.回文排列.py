from collections import defaultdict


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        single = 0
        cnt = defaultdict(int)

        for c in s:
            cnt[c] += 1
            if cnt[c] % 2 == 1:
                single += 1
            else:
                single -= 1

        if single <= 1:
            return True
        else:
            return False
