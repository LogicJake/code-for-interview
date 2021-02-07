from typing import List
import heapq


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        heap = [-x for x in arr[:k]]

        heapq.heapify(heap)

        for i in range(k, len(arr)):
            if arr[i] < -heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -arr[i])

        return [-x for x in heap]
