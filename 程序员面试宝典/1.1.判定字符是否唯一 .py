class Solution:
    def isUnique(self, astr: str) -> bool:
        mask = 0

        for c in astr:
            num = ord(c) - ord('a')
            if mask & (1 << num) != 0:
                return False
            else:
                mask = mask | (1 << num)
        return True


if __name__ == "__main__":
    solu = Solution()
    ans = solu.isUnique('leetcode')
    print(ans)
