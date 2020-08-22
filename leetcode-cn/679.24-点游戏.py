#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 点游戏
#

# @lc code=start
from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        EPSILON = 1e-6

        def solve(nums):
            if not nums:
                return False

            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON

            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i != j:
                        new_nums = []
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                new_nums.append(z)
                        for k in range(4):
                            if k < 2 and i > j:
                                continue
                            if k == 0:
                                new_nums.append(x + y)
                            elif k == 1:
                                new_nums.append(x * y)
                            elif k == 2:
                                new_nums.append(x - y)
                            elif k == 3:
                                if abs(y) < EPSILON:
                                    continue
                                new_nums.append(x / y)

                            if solve(new_nums):
                                return True

                            new_nums.pop()
            return False

        return solve(nums)


# @lc code=end
