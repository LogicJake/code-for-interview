class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        j = len(S) - 1
        i = length - 1

        S = list(S)

        while i >= 0 and j >= 0:
            if S[i] != ' ':
                S[j] = S[i]
                i -= 1
                j -= 1
            else:
                S[j] = '0'
                j -= 1
                S[j] = '2'
                j -= 1
                S[j] = '%'
                j -= 1

                i -= 1

        return ''.join(S[j + 1:])
