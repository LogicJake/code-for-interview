#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc = True
        des = True

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                des = False

            if A[i] < A[i - 1]:
                inc = False

        return inc or des


# @lc code=end
