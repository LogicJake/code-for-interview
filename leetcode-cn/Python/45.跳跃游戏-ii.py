#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        max_ = 0
        ans = 0
        n = len(nums)

        for i in range(n - 1):
            max_ = max(max_, i + nums[i])
            if i == end:
                end = max_
                ans += 1

        return ans


# @lc code=end
