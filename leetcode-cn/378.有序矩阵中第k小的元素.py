#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#

# @lc code=start
from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                if len(heap) < k:
                    heapq.heappush(heap, -matrix[i][j])
                else:
                    if matrix[i][j] < -heap[0]:
                        heapq.heappop(heap)
                        heapq.heappush(heap, -matrix[i][j])

        return -heap[0]


# @lc code=end
