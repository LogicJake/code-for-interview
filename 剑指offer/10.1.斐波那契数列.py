class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        ans = 0
        pre0 = 0
        pre1 = 1

        for _ in range(2, n + 1):
            ans = pre0 + pre1
            pre0 = pre1
            pre1 = ans

        return ans % 1000000007
