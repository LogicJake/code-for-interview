#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#

# @lc code=start
from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        for i in range(n):
            left = 0
            right = n - 1

            while left < right:
                if A[i][right] == A[i][left]:
                    A[i][right] ^= 1
                    A[i][left] ^= 1

                right -= 1
                left += 1

            if left == right:
                A[i][left] ^= 1
        return A


# @lc code=end
