class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def digist_sum(num):
            sum_ = 0

            while num != 0:
                sum_ += num % 10
                num = num // 10

            return sum_

        visited = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or digist_sum(
                    i) + digist_sum(j) > k or (i, j) in visited:
                return 0

            visited.add((i, j))

            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(
                i, j - 1)

        return dfs(0, 0)
