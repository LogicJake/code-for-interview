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
        ans = 0

        for i in range(1, n - 1):
            if A[i - 1] < A[i] and A[i + 1] < A[i]:
                j = i - 1
                k = i + 1

                while j >= 0 and A[j] < A[j + 1]:
                    j -= 1

                while k <= n - 1 and A[k] < A[k - 1]:
                    k += 1

                ans = max(ans, k - j - 1)
        return ans


# @lc code=end
