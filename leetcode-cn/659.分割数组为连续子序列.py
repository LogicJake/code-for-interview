#
# @lc app=leetcode.cn id=659 lang=python3
#
# [659] 分割数组为连续子序列
#

# @lc code=start
from typing import List
import heapq
from typing import DefaultDict


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        mp = DefaultDict(list)

        for num in nums:
            queue = mp[num - 1]

            if queue:
                pre_len = heapq.heappop(queue)
                heapq.heappush(mp[num], pre_len + 1)
            else:
                heapq.heappush(mp[num], 1)

        for queue in mp.values():
            if queue and queue[0] < 3:
                return False

        return True


# @lc code=end
