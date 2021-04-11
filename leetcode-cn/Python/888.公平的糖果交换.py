#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果交换
#

# @lc code=start
from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_A = sum(A)
        sum_B = sum(B)

        mem = set()
        for num in A:
            mem.add(num)

        for num in B:
            x = num + (sum_A - sum_B) // 2
            if x in mem:
                return [x, num]


# @lc code=end
