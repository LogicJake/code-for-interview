#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#

# @lc code=start
from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        A.sort()
        for i in range(len(A) - 1, 1, -1):
            if A[i - 2] + A[i - 1] > A[i]:
                return A[i - 2] + A[i - 1] + A[i]

        return 0


# @lc code=end
