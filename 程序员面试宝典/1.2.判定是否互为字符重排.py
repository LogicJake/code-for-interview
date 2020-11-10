class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        cnt = [0] * 26

        if len(s1) != len(s2):
            return False

        for i in range(len(s1)):
            o1 = ord(s1[i]) - ord('a')
            o2 = ord(s2[i]) - ord('a')

            cnt[o1] += 1
            cnt[o2] -= 1

        for i in range(26):
            if cnt[i] != 0:
                return False

        return True
