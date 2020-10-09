#
# @lc app=leetcode.cn id=1608 lang=python3
#
# [1608] 特殊数组的特征值
#

# @lc code=start
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = {i: 0 for i in range(n + 1)}

        for num in nums:
            k = min(num, n)
            ans[k] += 1

        cnt = 0
        for i in range(n, -1, -1):
            cnt += ans[i]
            if cnt == i:
                return i

        return -1


# @lc code=end
