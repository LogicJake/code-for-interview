#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

# @lc code=start
from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)

        if n <= 2:
            return False

        if A[1] <= A[0]:
            return False

        i = 1

        while i < n and A[i] > A[i - 1]:
            i += 1

        if i == n:
            return False

        while i < n and A[i] < A[i - 1]:
            i += 1

        return i == n


# @lc code=end
