#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start

from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int,
                      c: int) -> List[List[int]]:
        m = len(nums)
        n = len(nums[0])

        if m * n != r * c:
            return nums

        total = []
        for row in nums:
            total = total + row

        ans = []

        for i in range(r):
            ans.append(total[c * i:c * i + c])

        return ans


# @lc code=end
