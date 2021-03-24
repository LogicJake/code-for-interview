#
# @lc app=leetcode.cn id=456 lang=python3
#
# [456] 132模式
#

# @lc code=start
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        min_ = [float('inf')] * n

        for i in range(1, n):
            min_[i] = min(min_[i - 1], nums[i - 1])

        # 单调递减栈
        stack = []
        for j in range(n - 1, -1, -1):
            num_j = nums[j]
            num_k = float('-inf')
            while stack and stack[-1] < num_j:
                num_k = stack.pop(-1)
            stack.append(num_j)
            num_i = min_[j]

            if num_k > num_i:
                return True

        return False


# @lc code=end
