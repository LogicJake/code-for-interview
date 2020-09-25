#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的K对数字
#

# @lc code=start
from typing import List
import heapq


class Solution:
    '''
    维护大顶堆，比堆顶小则删除堆顶，并入栈
    '''
    def kSmallestPairs(self, nums1: List[int], nums2: List[int],
                       k: int) -> List[List[int]]:
        heap = []

        for num1 in nums1:
            for num2 in nums2:
                if len(heap) != k:
                    heapq.heappush(heap, (-(num1 + num2), [num1, num2]))
                else:
                    if num1 + num2 < -heap[0][0]:
                        heapq.heappop(heap)
                        heapq.heappush(heap, (-(num1 + num2), [num1, num2]))

        return [item[1] for item in heap]


# @lc code=end
