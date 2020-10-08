# -*- coding:utf-8 -*-
import heapq


class Finder:
    def findKth(self, a, n, K):
        heap = []
        for i in range(n):
            if len(heap) < K:
                heapq.heappush(heap, a[i])
            elif a[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, a[i])

        return heap[0]


if __name__ == "__main__":
    a = [1, 3, 5, 2, 2]
    n = 5
    K = 3

    algo = Finder()
    ans = algo.findKth(a, n, K)
    print(ans)
