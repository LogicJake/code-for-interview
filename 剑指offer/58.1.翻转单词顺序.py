class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()

        i = j = len(s) - 1
        words = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            words.append(s[i + 1:j + 1])

            while i >= 0 and s[i] == ' ':
                i -= 1