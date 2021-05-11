class Solution:
    def compressString(self, S: str) -> str:
        ans = ''
        pre = ''
        cnt = 0
        for c in S:
            if c != pre:
                if pre != '':
                    ans += pre
                    ans += str(cnt)

                pre = c
                cnt = 1
            else:
                cnt += 1

        if pre != '':
            ans += pre
            ans += str(cnt)

        if len(ans) >= len(S):
            return S
        else:
            return ans
