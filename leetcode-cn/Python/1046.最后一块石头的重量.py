#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) >= 2:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)

            if stone1 != stone2:
                heapq.heappush(heap, -(abs(stone1 - stone2)))

        if len(heap) == 0:
            return 0
        return -heap[0]


# @lc code=end
