#
# @lc app=leetcode.cn id=845 lang=python3
#
# [845] 数组中的最长山脉
#

# @lc code=start
from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)

        left = [0] * n
        right = [0] * n

        for i in range(1, n):
            if A[i] > A[i - 1]:
                left[i] = left[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if A[i] > A[i + 1]:
                right[i] = right[i + 1] + 1

        ans = 0
        for i in range(n):
            if left[i] > 0 and right[i] > 0:
                ans = max(ans, left[i] + right[i] + 1)

        return ans


# @lc code=end
