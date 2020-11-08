class Solution:
    def replaceSpace(self, s: str) -> str:
        ans = ['0'] * (len(s) * 3)

        sz = 0

        for c in s:
            if c == ' ':
                ans[sz] = '%'
                sz += 1
                ans[sz] = '2'
                sz += 1
                ans[sz] = '0'
                sz += 1
            else:
                ans[sz] = c
                sz += 1

        return ''.join(ans[:sz])


if __name__ == "__main__":
    solution = Solution()
    s = "We are happy."
    ans = solution.replaceSpace(s)
    print(ans)