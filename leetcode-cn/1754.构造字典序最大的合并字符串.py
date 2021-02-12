class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        merge = []

        def help(s, t):
            i = 0

            while i < len(s) and i < len(t):
                if s[i] > t[i]:
                    return True
                elif s[i] < t[i]:
                    return False

                i += 1

            if i < len(s):
                return True

            return False

        while i < len(word1) or j < len(word2):
            if help(word1[i:], word2[j:]):
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word2[j])
                j += 1

        return ''.join(merge)
