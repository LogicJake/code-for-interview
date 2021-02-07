class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        arr = [a, b, c]
        arr.sort()

        max1 = arr[-1]
        max2 = arr[-2]
        min = arr[0]

        t = (max1 - max2 + min) // 2

        ans = max1 - t
        print(ans)
