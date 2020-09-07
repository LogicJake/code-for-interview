#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
from typing import List
import heapq


class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     cnt = {}
    #     for num in nums:
    #         if num not in cnt:
    #               cnt[num] = 1
    #         else:
    #             cnt[num] += 1

    #     backet = [None] * len(nums)
    #     for key in cnt:
    #         if backet[cnt[key]] is None:
    #             backet[cnt[key]] = []

    #         backet[cnt[key]].append(key)

    #     res = []
    #     i = len(backet) - 1
    #     while len(res) < k and i > -1:
    #         if backet[i] is not None:
    #             for num in backet[i]:
    #                 res.append(num)
    #         i -= 1

    #     return res[:k]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for num in nums:
            if num not in cnt:
                cnt[num] = 1
            else:
                cnt[num] += 1

        heap = []
        for num in cnt:
            if len(heap) < k:
                heapq.heappush(heap, (cnt[num], num))
            else:
                if cnt[num] > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (cnt[num], num))

        res = []
        for e in heap:
            res.append(e[1])
        return res


# @lc code=end
