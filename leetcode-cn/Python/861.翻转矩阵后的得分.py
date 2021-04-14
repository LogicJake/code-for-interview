#
# @lc app=leetcode.cn id=861 lang=python3
#
# [861] 翻转矩阵后的得分
#

# @lc code=start
from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])

        ans = m * 2**(n - 1)

        for i in range(1, n):
            nums = 0

            for j in range(m):
                if A[j][0] == 1:
                    nums += A[j][i]
                else:
                    nums += 1 - A[j][i]

            nums = max(nums, m - nums)
            ans += nums * 2**(n - 1 - i)

        return ans


# @lc code=end
