#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#

# @lc code=start
from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        right = 0
        ans = 0

        mem = []
        while right < len(A):
            if A[right] == 0:
                mem.append(right)

            right += 1

            if len(mem) > K:
                left = mem[0] + 1
                mem.pop(0)

            ans = max(ans, right - left)

        return ans


# @lc code=end
