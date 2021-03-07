#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        ans = [-1] * n

        for i in range(2 * n - 1):
            index = i % n
            while stack and nums[stack[-1]] < nums[index]:
                ans[stack.pop(-1)] = nums[index]
            stack.append(index)
        return ans


# @lc code=end
