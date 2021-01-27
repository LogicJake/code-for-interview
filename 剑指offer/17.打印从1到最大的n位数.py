from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        max_num = 10**n - 1

        return list(range(1, max_num + 1))
