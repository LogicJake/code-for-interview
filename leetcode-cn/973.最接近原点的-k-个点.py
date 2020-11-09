#
# @lc app=leetcode.cn id=973 lang=python3
#
# [973] 最接近原点的 K 个点
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ans = []

        for point in points:
            dis = -(point[0]**2 + point[1]**2)

            if len(ans) < K:
                heapq.heappush(ans, [dis, point])
            else:
                if dis > ans[0][0]:
                    heapq.heappop(ans)
                    heapq.heappush(ans, [dis, point])

        return [a[1] for a in ans]


# @lc code=end
