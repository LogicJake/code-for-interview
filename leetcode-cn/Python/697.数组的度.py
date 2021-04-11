#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = {}
        cnt = defaultdict(int)
        max_degree = 0

        for index, num in enumerate(nums):
            if num not in degree:
                degree[num] = [-1, -1]

            if degree[num][0] == -1:
                degree[num][0] = index
                degree[num][1] = index
            else:
                degree[num][1] = index

            cnt[num] += 1
            max_degree = max(max_degree, cnt[num])

        ans = 999999
        for k, v in cnt.items():
            if v == max_degree:
                ans = min(ans, degree[k][1] - degree[k][0] + 1)
        return ans


# @lc code=end
