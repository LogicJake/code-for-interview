#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # upper = max(arr1)
        upper = 1000

        cnt = [0] * (upper + 1)

        for num in arr1:
            cnt[num] += 1

        ans = []
        for num in arr2:
            ans += [num] * cnt[num]
            cnt[num] = 0

        for num in range(upper + 1):
            if cnt[num] > 0:
                ans += [num] * cnt[num]

        return ans


# @lc code=end
